#!/usr/bin/env python3

from fib_brygg_from_cpp import fib_cpp
from fib import fib_py
from time import perf_counter as pc
import matplotlib.pyplot as plt

n1=30
n2=40
time_cpp=[]
n_cpp=[]
time_py=[]
n_py=[]
print('hej')
for n in range(n1,n2):

    print(f'fib(n) for C++ with n={n}' )
    start_cpp = pc()
    print(fib_cpp(n))
    end_cpp = pc()
    print(f'Time in seconds {round(end_cpp-start_cpp, 2)}')
    time_cpp.append(round(end_cpp-start_cpp, 2))
    n_cpp.append(n)

    print(f'fib(n) for py with n={n}' )
    start_py = pc()
    print(fib_py(n))
    end_py = pc()
    print(f'Time in seconds {round(end_py-start_py, 2)}')
    time_py.append(round(end_py-start_py, 2))
    n_py.append(n)


print(f'fib(n) for C++ with n=47')
start_cpp = pc()
print(fib_cpp(47))
end_cpp = pc()
print(f'Time in seconds {round(end_cpp-start_cpp, 2)}')

plt.plot(n_cpp,time_cpp ,'bo',n_py, time_py,'ro')
plt.savefig('fib_c.png')


