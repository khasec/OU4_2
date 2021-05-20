""" Python interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libfib.so')

lib.fib_cpp.argtypes = [ctypes.c_int]
lib.fib_cpp.restype = [ctypes.c_int]

def fib_cpp(n):
    return lib.fib_cpp(n)