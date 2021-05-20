//Fibonacci Series using Recursion
#include<bits/stdc++.h>
using namespace std;
 
int fib(int n)
{
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}
 
extern "C"{
    int fib_cpp(int n) {return fib(n);}
}