"""
Script to extract CNN features to numpy file using a caffe model.

Usage: python extract_features_to_numpy.py /path/to/image_list.jpg /path/to/images/ /path/to/numpy.npy
"""

from caffetools.extract.DeepFeatures import DeepFeatures
import argparse
import os
from tqdm import tqdm

# parse arguments
parser = argparse.ArgumentParser(description='Script to extract CNN features into numpy file')
parser.add_argument('images_list_path', help='path to text file of list of images')
parser.add_argument('images_path', help='path to base directory of images')
parser.add_argument('output_path', help='path to output numpy file')
args = parser.parse_args()

# check
if not os.path.exists(args.images_path):
	raise OSError('images_path does not exist: {0}'.format(args.images_path))

# open images list
with open(args.images_list_path, 'r') as f:
	images_list = [line.strip() for line in f]

# loop over images
d = DeepFeatures()
num_images = len(images_list)
data = None
for index, image in enumerate(tqdm(images_list)):
	path_to_image = os.path.join(args.images_path, image)

	# extract features
	features = d.extract_features(path_to_image)
	if not data:
		feature_dim = features.shape[0]
		data = np.zeros((num_images, feature_dim))

	# put in numpy matrix
	data[index, :] = features

# save to numpy file
np.save(args.output_path, data)
