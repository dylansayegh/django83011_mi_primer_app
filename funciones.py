def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

def suma(a, b):
    return a + b
    
