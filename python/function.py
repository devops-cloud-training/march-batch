# what is funtion?

def operations(x,y):
    c = x+y
    d= x-y
    e = x*y
    f = x/y
    print(c,d,e,f)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    operations(b,c)
except ValueError:
    print("Please enter only integer values!")



