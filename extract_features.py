"""
Script to extract CNN features using Googlenet.

Usage: python extract_features.py /path/to/input/image.jpg /path/to/output/features.txt
"""

from caffetools.extract.DeepFeatures import DeepFeatures
from caffetools.lmdb.numpyserializer import NumPySerializer
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Script to extract CNN features into LMDB')
parser.add_argument('input_image_path', help='path to input image')
parser.add_argument('output_features_path', help='path to output features text file')
args = parser.parse_args()

# extract features
d = DeepFeatures()
features = d.extract_features(args.input_image_path)

# save to text file
with open(args.output_features_path, 'w') as f:
	features_row_vector = features.reshape(1,-1)
	features_string = NumPySerializer.numpy_to_string(features_row_vector)
	f.write(features_string)
	print "Features saved to '%s'" % args.output_features_path

