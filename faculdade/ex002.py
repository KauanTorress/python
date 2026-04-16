m = dict()
def lista(l, n):
    if n == 1:
        return l[0]
    elif m.get(n) != None:
        return m[n]   
    else:
        m[n] = max(l[n-1], lista(l, n-1))
        return m[n]
    
l = [1, 5, 3, 9, 2]
n = len(l)
print(lista(l, n))