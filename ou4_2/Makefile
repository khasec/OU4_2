# Makefile for OU4
all:
	g++ -c -fPIC heltal.cpp -o heltal.o
	g++ -c -fPIC fib.cpp -o fib.o
	g++ -shared -o libheltal.so  heltal.o
	g++ -shared -o libfib.so fib.o		
clean:
	rm -fr *.o *.so __pycache__
