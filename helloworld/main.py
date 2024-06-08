
from dask.distributed import Client

import tensorflow as tf

def main():
    client = Client()
    num_devices = len(tf.config.list_physical_devices('GPU'))
    print('num devices: ', num_devices)
    client.close()

if __name__ == '__main__':
    main()