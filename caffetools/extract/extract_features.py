"""
Script to extract CNN features using Googlenet.

Usage: python extract_features.py /path/to/input/image.jpg /path/to/output/features.txt
"""

from DeepFeatures import DeepFeatures
import sys

if len(sys.argv) < 3:
	raise ValueError('invalid number of arguments')

input_image_path = sys.argv[1]
output_features_path = sys.argv[2]

d = DeepFeatures()
features = d.extract_features(input_image_path)
d.save_features_to_text_file(features, output_features_path)

