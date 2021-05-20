""" Python interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libfib.so')

lib.fib.argtypes = [ctypes.c_int]
lib.fib.restype = [ctypes.c_int]

def fib_cpp(n):
    return lib.fib(n)