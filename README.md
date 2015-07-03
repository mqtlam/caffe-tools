# caffe-tools
Deep learning tools using caffe

- utilities for extracting deep features from images [(more info)](caffetools/extract/README.md)
- utilities for storing and retrieving deep features into and from LMDB databases [(more info)](caffetools/lmdb/README.md)

## usage
All tools are intended to be used from the root directory of caffe-tools unless otherwise specified. We denote this uppermost directory as `$ROOT`.

## configuration
Before using any tool, make sure to set up the configuration file `config.json`. You can copy `config.json.template` and make the appropriate changes.

## library
If you add `$ROOT` to your PYTHONPATH, you can run `import caffetools` to import the package into your code.
