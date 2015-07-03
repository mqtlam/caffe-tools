"""
Convert caffe mean file from .binaryproto to .npy
Usage: python convert_protomean.py /path/to/proto.mean /path/to/out.npy
"""

import numpy as np
import sys

# load settings
import config
config = config.load_settings()

# load caffe
sys.path.insert(0, config['path']['caffe_root'] + '/python')
import caffe

# parse arguments
if len(sys.arg) != 3:
	print "Usage: python convert_protomean.py /path/to/proto.mean /path/to/out.npy"
	sys.exit()
input_file = sys.argv[1]
output_file = sys.argv[2]

# convert script
blob = caffe.proto.caffe_pb2.BlobProto()
data = open(input_file, 'rb').read()
blob.ParseFromString(data)
arr = np.array(caffe.io.blobproto_to_array(blob))
out = arr[0]
np.save(output_file, out)

