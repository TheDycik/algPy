import sys

def count_size(x):
    size = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items:
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size

# '3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] win32'