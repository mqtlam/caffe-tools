import numpy as np
from tempfile import TemporaryFile

class NumPySerializer():
	"""Static methods to convert and serialize numpy arrays.
	
	"""
	@staticmethod
	def serialize_numpy(array):
		"""Serialize numpy array into string.
		
		Good for storing into a database.
		
		Args:
			array (numpy): numpy array to serialize

		Returns:
			serialized numpy array as string

		"""
		f = TemporaryFile()
		np.save(f, array)
		f.seek(0)
		string = f.read()
		return string

	@staticmethod
	def unserialize_numpy(string):
		"""Unserialize string into numpy array.
		
		Args:
			string (string): string to unserialize

		Returns:
			numpy array

		"""
		f = TemporaryFile()
		f.write(string)
		f.seek(0)
		array = np.load(f)
		return array

	@staticmethod
	def numpy_to_string(array):
		"""Convert numpy array into human-readable string.
		
		Good for passing to other programs.

		Notes:
			human-readable string example:
				1 2 3
				4 5 6
			is a string for the following array:
				[[1,2,3]
				 [4,5,6]]

		Args:
			array (numpy): array to convert to human-readable string

		Returns:
			human-readable string of array

		"""
		f = TemporaryFile()
		np.savetxt(f, array, fmt='%.8g')
		f.seek(0)
		string = f.read()
		return string

	@staticmethod
	def string_to_numpy(string):
		"""Convert human-readable string into numpy array.
		
		Note:
			loads as floats even if stored as ints. 
			
			human-readable string example:
				1 2 3
				4 5 6
			is a string for the following array:
				[[1,2,3]
				 [4,5,6]]
		
		Args:
			string (string): human-readable string to convert to numpy array

		Returns:
			numpy array

		"""
		f = TemporaryFile()
		f.write(string)
		f.seek(0)
		array = np.loadtxt(f)
		return array
	
