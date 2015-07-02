"""
Convert caffe mean file from .binaryproto to .npy.
"""

import caffe
import numpy as np
import sys

if len(sys.arg) != 3:
	print "Usage: python /mean/convert_protomean.py proto.mean out.npy"
	sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

blob = caffe.proto.caffe_pb2.BlobProto()
data = open(input_file, 'rb').read()
blob.ParseFromString(data)
arr = np.array(caffe.io.blobproto_to_array(blob))
out = arr[0]
np.save(output_file, out)
