import numpy as np
from tempfile import TemporaryFile

class NumpySerializer():
	"""
	Static methods to convert and serialize Numpy arrays.
	"""
	@staticmethod
	def serialize_numpy(array):
		"""
		Serialize numpy array into string.
		Good for storing into a database.
		"""
		f = TemporaryFile()
		np.save(f, array)
		f.seek(0)
		string = f.read()
		return string

	@staticmethod
	def unserialize_numpy(string):
		"""
		Unserialize string into numpy array.
		"""
		f = TemporaryFile()
		f.write(string)
		f.seek(0)
		array = np.load(f)
		return array

	@staticmethod
	def numpy_to_string(array):
		"""
		Convert numpy array into human-readable string.
		Good for passing to other programs.
		"""
		f = TemporaryFile()
		np.savetxt(f, array, fmt='%.8g')
		f.seek(0)
		string = f.read()
		return string

	@staticmethod
	def string_to_numpy(string):
		"""
		Convert human-readable string into numpy array.
		Warning: loads as floats even if stored as ints. 
		"""
		f = TemporaryFile()
		f.write(string)
		f.seek(0)
		array = np.loadtxt(f)
		return array
	
