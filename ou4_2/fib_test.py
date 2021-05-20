#!/usr/bin/env python3

from fib_brygg_from_cpp import fib_cpp
from fib import fib_py
from time import perf_counter as pc

n1=30
n2=45
for n in range(n1,n2):

    print(f'fib(n) for C++ with n={n}' )
    start_cpp = pc()
    print(fib_cpp(n))
    end_cpp = pc()
    print(f'Time in seconds {round(end_cpp-start_cpp, 2)}')

    print(f'fib(n) for py with n={n}' )
    start_py = pc()
    print(fib_py(n))
    end_py = pc()
    print(f'Time in seconds {round(end_py-start_py, 2)}')


print(f'fib(n) for C++ with n=47')
start_cpp = pc()
print(fib_cpp(47))
end_cpp = pc()
print(f'Time in seconds {round(end_cpp-start_cpp, 2)}')
