"""
Script to extract CNN features using Googlenet.

Usage: python extract_features.py /path/to/input/image.jpg /path/to/output/features.txt
"""

from caffetools.extract.DeepFeatures import DeepFeatures
from caffetools.lmdb.numpyserializer import NumPySerializer
import sys

# parse arguments
if len(sys.argv) < 3:
	raise ValueError('invalid number of arguments')
input_image_path = sys.argv[1]
output_features_path = sys.argv[2]

# extract features
d = DeepFeatures()
features = d.extract_features(input_image_path)

# save to text file
with open(output_features_path, 'w') as f:
	features_row_vector = features.reshape(1,-1)
	features_string = NumPySerializer.numpy_to_string(features_row_vector)
	f.write(features_string)
	print "Features saved to '%s'" % output_features_path

