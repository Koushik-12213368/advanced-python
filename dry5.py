'''def check():
    a=int(input("enter value:"))
    if a%2==0:
        print("the number is even")
    else:
        print("the number is odd")
check(a)
'''
'''def swap(a,b):
    a,b=b,a
    return(a,b)
a=int(input("enter the value"))
b=int(input("enter the value"))
print("before swaping",a,b)
a,b=swap(a,b)
print("after swaping",a,b)'''
   
'''def square(x):
    x=x**2
    return x
def double(x):
    x=x*2
    return x
def cube(x):
    x=x**3
    return x
x=int(input("enter:"))
print("double,squaring the value:",square(double(cube(x))))'''



'''def square(x):
    x=x**2
    return x
def double(x):
    x=x*2
    return x
def cube(x):
    x=x**3
    return x
x=int(input("enter:"))
composed=compose(square,double,cube)
print(composed)'''

def compose(functions):
def inner():
arg for f in reversed(functions):
arg = f(arg)
return arg
return inner
def square(x):
return x*2
def increment(x):
return x+1
def half(x):
return x/2




composed = compose(square, increment, half)
print(composed(5))
composed = compose(square, increment)
print(composed(5))
