def upcase(func):
    def intern(*args, **kwargs):
        print(args[0].upper())
        return func(*args, **kwargs)
    return intern

@upcase
def conta(x):
    return x
   

conta("gabriel")
