import pickle
import os

from definitions import ROOT_DIR


def bitify(s):
    return ''.join(format(c, 'b') for c in bytearray(s, 'utf-8'))


def load_primes():
    with open(os.path.join(ROOT_DIR, 'resources/primes.bin'), 'rb') as f:
        primes = pickle.load(f)
    return primes


def binary_search(array, element, start=0, end=None):
    end = end or len(array) - 1

    if start > end:
        return False, end

    mid = (start + end) // 2
    if element == array[mid]:
        return True, mid

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)
