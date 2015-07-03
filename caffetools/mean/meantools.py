import numpy as np
import sys

# load settings
import config
config = config.load_settings()

# load caffe
sys.path.insert(0, config['path']['caffe_root'] + '/python')
import caffe

class MeanTools:
	"""
	Static methods for creating and converting mean files
	"""
	@staticmethod
	def convert_binaryproto_to_npy(input_file, output_file):
		blob = caffe.proto.caffe_pb2.BlobProto()
		data = open(input_file, 'rb').read()
		blob.ParseFromString(data)
		arr = np.array(caffe.io.blobproto_to_array(blob))
		out = arr[0]
		np.save(output_file, out)
		print "Converted mean file from binaryproto to npy."

