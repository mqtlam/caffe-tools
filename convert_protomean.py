"""
Convert caffe mean file from .binaryproto to .npy
Usage: python convert_protomean.py /path/to/proto.mean /path/to/out.npy
"""
import sys
from caffetools.mean.meantools import MeanTools

# parse arguments
if len(sys.argv) != 3:
	print "Usage: python convert_protomean.py /path/to/proto.mean /path/to/out.npy"
	sys.exit()
input_file = sys.argv[1]
output_file = sys.argv[2]

# convert
MeanTools.convert_binaryproto_to_npy(input_file, output_file)

