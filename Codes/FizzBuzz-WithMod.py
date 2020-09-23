import sys

def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            sys.stdout.write("FizzBuzz\n")
        if i%3 == 0 and i%5 != 0:
            sys.stdout.write("Fizz\n")
        if i%3 != 0 and i%5 == 0:
            sys.stdout.write("Buzz\n")
        if i%3 != 0 and i%5 != 0:
            sys.stdout.write(str(i)+"\n")