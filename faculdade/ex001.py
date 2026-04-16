#código sem memoização

def fibonacci(n) :
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))

#código com memoização
m = dict()
def fibonacci_mem(n):
    if n <= 1:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
       m[n] = fibonacci_mem(n-1) + fibonacci_mem(n-2)
       return m[n]