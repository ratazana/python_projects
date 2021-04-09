def upcase(func):
    def intern(*args, **kwargs):
        for name in args:
            print(name.upper())
        return func(*args, **kwargs)
    return intern

@upcase
def conta(*x):
    return x
   

conta("gabriel", "machado")
