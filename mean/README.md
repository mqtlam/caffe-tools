# mean utilities
Utilities for creating and modifying mean files for caffe usage

## convert from binaryproto to npy
A utility is included to convert a mean file from .binaryproto format (generated from caffe's `compute_image_mean.bin`) to numpy format. This is necessary for the [deep features extraction code](../extract/README.md).

Usage: `python mean/convert_protomean.py /path/to/input/proto/mean.binaryproto /path/to/output/numpy/mean.npy`
