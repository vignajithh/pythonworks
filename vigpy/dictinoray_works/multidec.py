def decor1(f):
    def inner():
        x=f()
        return x*x
    return inner

def decor2(f):
    def inner():
        x=f()
        return 2*x
    return inner
@decor1
@decor2
def num():
    return 10

print(num())