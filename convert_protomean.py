"""
Convert caffe mean file from .binaryproto to .npy
Usage: python convert_protomean.py /path/to/imagenet_mean.binaryproto /path/to/output.npy
"""
import sys
from caffetools.mean.meantools import MeanTools
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Convert caffe mean file from .binaryproto to .npy')
parser.add_argument('binaryproto_file', help='path to imagenet_mean.binaryproto')
parser.add_argument('npy_file', help='path to output.npy')
args = parser.parse_args()

# convert
MeanTools.convert_binaryproto_to_npy(args.binaryproto_file, args.npy_file)

