import numpy as np
import sys

# load settings
import config
config = config.load_settings()

# load caffe
import os
sys.path.insert(0, os.path.join(config['path']['caffe_root'], 'python'))
import caffe

class MeanTools:
	"""Static methods for creating and converting mean files.
	
	"""
	@staticmethod
	def convert_binaryproto_to_npy(input_file, output_file):
		"""Convert binaryproto file to npy file.

		Args:
			input_file (string): path to .binaryproto input file
			output_file (string): path to .npy file for output

		"""
		blob = caffe.proto.caffe_pb2.BlobProto()
		data = open(input_file, 'rb').read()
		blob.ParseFromString(data)
		arr = np.array(caffe.io.blobproto_to_array(blob))
		out = arr[0]
		np.save(output_file, out)
		print "Converted mean file from binaryproto to npy."

