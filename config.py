import json

DEFAULT_CONFIG_FILE_PATH = 'config.json'

def load_settings(config_file_path = DEFAULT_CONFIG_FILE_PATH):
	"""
	Load settings from config JSON file.
	"""
	with open(config_file_path, 'r') as f:
		config = json.load(f)
	for i in config:
		for j in config[i]:
			if isinstance(config[i][j], basestring):
				config[i][j] = config[i][j].encode('ascii', errors='backslashreplace')
	return config

