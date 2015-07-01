import json

def load_settings():
	"""
	Load settings from config JSON file.
	"""
	with open('config.json') as f:
		config = json.load(f)
	for i in config:
		for j in config[i]:
			if isinstance(config[i][j], basestring):
				config[i][j] = config[i][j].encode('ascii', errors='backslashreplace')
	return config

