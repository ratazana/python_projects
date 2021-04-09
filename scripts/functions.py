

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

def arrangement(n, k):
    return factorial(n) / factorial(n-k)
