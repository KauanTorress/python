m = dict()
def lista_soma(l, n):
    if n == 1:
        return l[0]
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = l[n-1] + lista_soma(l, n-1)
        return m[n]
    
l = [1, 5, 4, 9, 3]
n = len(l)
print(lista_soma(l, n))
