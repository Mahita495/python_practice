def new_decorator(x):
    def add(y):
        return x+y
    return add

a=new_decorator(5)
print(a(6))


def shout(txt):
    return txt.lower()
def laugh(txt):
    return txt.upper()

def greet(func):
    greeting=func("This is a type of greeting")
    print(greeting)

greet(shout)
greet(laugh)
