# lmdb tools 
LMDB tools provides an easy way to store and retrieve caffe features using a LMDB database

[(up)](../../README.md)

## NumPy Serializer
A utility class is provided to serialize and unserialize NumPy arrays for storing into LMDB databases. It can also convert NumPy array into human-readable strings for passing into other programs.

## API
Assuming your PYTHONPATH is set up properly (e.g. you are currently in the `$ROOT` directory), you can use the LMDBTools API calls as follows:

```python
from caffetools.lmdb import lmdbtools as l
from caffetools.lmdb.numpyserializer import NumPySerializer as n
import numpy as np

with l.open('/path/to/lmdb') as db:
	# example
	key = 'image1'
	value = np.arange(10)

	# add an entry
	serialized_value = n.serialize_numpy(value)
	db.put(key, serialized_value)

	# get entry
	serialized_value = db.get(key)
	value = n.unserialize_numpy(serialized_value)

	# print entries
	db.print_entries()

	# print keys
	db.print_keys()

	# dump all data into a dictionary
	dictionary = db.dump()

	# delete entry
	db.delete(key)
```
