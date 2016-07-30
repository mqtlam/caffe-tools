"""
Script to extract CNN features using Googlenet.

Usage: python extract_features_to_lmdb.py /path/to/image_list.jpg /path/to/images/ /path/to/lmdb
"""

from caffetools.extract.DeepFeatures import DeepFeatures
from caffetools.lmdb import lmdbtools
from caffetools.lmdb.numpyserializer import NumPySerializer
import argparse
import os

# parse arguments
parser = argparse.ArgumentParser(description='Script to extract CNN features into LMDB')
parser.add_argument('images_list_path', help='path to text file of list of images')
parser.add_argument('images_path', help='path to base directory of images')
parser.add_argument('lmdb_path', help='path to output lmdb')
args = parser.parse_args()

# check
if not os.path.exists(args.images_path):
	raise OSError('images_path does not exist: {0}'.format(args.images_path))

# open images list
with open(args.images_list_path, 'r') as f:
	images_list = [line.strip() for line in f]

# loop over images
d = DeepFeatures()
for image in images_list:
	path_to_image = os.path.join(args.images_path, image)

	# extract features
	features = d.extract_features(path_to_image)
	serialized_features = NumpySerializer.serialize_numpy(features)

	# save to lmdb
	with lmdbtools.open(args.lmdb_path) as db:
		if db.get(image): 
			db.put(image, serialized_features)
			if db.get('count'):
				db.put('count', 1)
			else:
				count = db.get('count')
				db.put('count', count+1)

