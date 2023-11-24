import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return(n*factorial(n-1))

def factorial2(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    a = 0
    b = 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b

t1 = time.time()
print(fib2(1000))
t2 = time.time()
print(t2-t1)