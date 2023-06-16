import tensorflow as tf
import keras
from tensorflow.python.client import device_lib

print(tf.__version__)
print(keras.__version__)

print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))

print(device_lib.list_local_devices())