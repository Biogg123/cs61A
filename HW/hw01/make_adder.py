def make_adder(n):
    def adder(k):
        return k+n
    return adder

add_three= make_adder(3)
#print(add_three(4))

def square(x):
    return x*x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

#squadder=compose1(square, make_adder(2))
#print(squadder(3))

def f(x):
    return g(x-1)

def g(y):
    return abs(h(y)-h(1/y))

def h(z):
    return z*z

#print(f(1))

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate=cake()

#chocolate




x,y=1,1
def m():
    add=1
    def add(x,y):
        return x+y
    return 

print(m)
print(add)

