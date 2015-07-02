import lmdb

class LMDBTools(object):
	"""
	LMDBTools is a wrapper helper class for working with LMDB databases.
	"""
	def __init__(self, dbpath):
		self.dbpath = dbpath
		self.env = None
		self.map_size = pow(2, 40)

	def __enter__(self):
		self.env = lmdb.open(self.dbpath, map_size=self.map_size)
		return self

	def __exit__(self, type, value, traceback):
		self.env.close()

	def put(self, key, value):
		"""
		Put key, value into the database.
		"""
		with self.env.begin(write=True) as txn:
			result = txn.put(key, value)
		return result

	def get(self, key):
		"""
		Get the value indexed by key in the database.
		"""
		with self.env.begin(write=False) as txn:
			value = txn.get(key)
		return value

	def delete(self, key):
		"""
		Delete the key in the database.
		"""
		with self.env.begin(write=True) as txn:
			result = txn.delete(key)
		return result

	def dump(self):
		"""
		Print all (key,value) pairs in the database.
		"""
		with self.env.begin(write=False) as txn:
			cursor = txn.cursor()
			for key, value in cursor:
				print (key, value)

	def dump_keys(self):
		"""
		Print all keys in the database.
		"""
		with self.env.begin(write=False) as txn:
			cursor = txn.cursor()
			for key, _ in cursor:
				print key

def open(dbpath):
	"""
	API for LMDB operations.

	Usage: 	with lmdbtools.open('/path/to/lmdb') as db:
			db.put(key, value)
			db.get(key)
			...
	"""
	return LMDBTools(dbpath)

