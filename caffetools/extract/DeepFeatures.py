import numpy as np
import sys

# load settings
import config
config = config.load_settings()

# load caffe
import os
sys.path.insert(0, os.path.join(config['path']['caffe_root'], 'python'))
import caffe

class DeepFeatures:
	"""A class for extracting deep features from images using caffe.
	
	"""
	def __init__(self):
		self.layer_name = config['extract']['layer_name']
		self._init_caffe_net()
		print "Finished initialization. Ready to extract features."

	def _init_caffe_net(self):
		"""Helper function for initializing caffe network.
		
		"""
		caffe.set_mode_gpu()
		self.net = caffe.Net(config['path']['deploy'],
				config['path']['caffemodel'],
				caffe.TEST)

		# input data processing: 'data' is the name of the input blob == net.inputs[0]
		self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
		self.transformer.set_transpose('data', (2,0,1))
		self.transformer.set_mean('data', np.load(config['path']['mean_npy_file']).mean(1).mean(1)) # mean pixel
		self.transformer.set_raw_scale('data', 255) # the reference model operates on images in [0,255] range instead of [0,1]
		self.transformer.set_channel_swap('data', (2,1,0)) # the reference model has channels in BGR order instead of RGB

	def extract_features(self, image_file):
		"""Extract deep features from an input image.

		Args:
			image_file (string): path to image file

		Returns:
			deep features of image

		"""
		batch_size = 1
		self.net.blobs['data'].reshape(batch_size, 3, config['extract']['input_size'][0], config['extract']['input_size'][1])

		# load image
		self.net.blobs['data'].data[...] = self.transformer.preprocess('data', caffe.io.load_image(image_file))

		# feed forward to get activations for features
		out = self.net.forward()

		# get features from specified layer
		features = self.net.blobs[self.layer_name].data[0]
		return features

	def extract_features_batch(self, image_files_list):
		"""Extract batch of deep features from a list of input images.

		Args:
			image_files_list (list): list of image paths

		Returns:
			deep features of images

		"""
		batch_size = len(image_files_list)
		self.net.blobs['data'].reshape(batch_size, 3, config['extract']['input_size'][0], config['extract']['input_size'][1])

		# load image
		self.net.blobs['data'].data[...] = map(lambda x: self.transformer.preprocess('data', caffe.io.load_image(x)), image_files_list)

		# feed forward to get activations for features
		out = self.net.forward()

		# get features from specified layer
		features = self.net.blobs[self.layer_name].data
		return features

