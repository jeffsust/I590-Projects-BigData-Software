import sys

def fizzbuzz(n):
  
    # write a python program called fizzbuzz.py that accepts an integer 
    # n from the command line. Pass this integer to a function called 
    # fizzbuzz. The fizzbuzz function should then iterate from 1 to n. 
    # If the ith number is a multiple of two, print fizz, if a 
    # multiple of three print buzz, if a multiple of both print 
    # fizzbuzz, else print the value.
       
    for i in range(1,n+1):
        if i % 6 == 0:
	    print "fizzbuzz"
        elif i % 3 == 0:
	    print "buzz"
	elif i % 2 == 0: 
	    print "fizz"
	else:
	    print i

if __name__ == '__main__':
    n = int(sys.argv[1])
    fizzbuzz(n) 
