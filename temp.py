def exefun(*functions):
    def fun(*args):
        if len(functions)!=len(args):
            return
        for i in range(len(functions)):
            yield functions[i](args[i])
    return fun
    
f = lambda a: print(a)
k = exefun(f)
print(list(k(4555)))