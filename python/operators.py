# Arithmetic operator

a = 10
b = 15

addition = a + b
sub=a-b
mul = a*b
div = a/b
power = a**2
rem = b%a
floordiv = b//a

print(addition, sub, mul, div, power, rem, floordiv)

# Assignment operator

a = 10
print(a)

a += 5 # a = a+5
print(a)
a -= 5 # a = a-5
print(a)
a *= 5 # a = a*5
print(a)
a /= 5 # a = a/5
print(a)
a %= 5 # a = a%5
print(a)
a **= 5 # a = a**5
print(a)

# comparison operator

a = 10
b = 15

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operator

# and or not
a = 15
b = 10
print(True and False)
print(True or False)
print(not True)
print(a>b and a%b<b)


# Bitwise operator

# & bitwise And
# | bitwise or
# ~ bitwise not
# ^ bitwise xor
# >> bitwise right shift
# << bitwise leftshift

a = 10 # 00001010
b = 4  # 00000100
# =====================
#     &  00000000
#     |  00001110
#     ~  11110101
#     ^  00001110
#     >> 00000010
#     << 00101000
# =====================
print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a>>2)
print(a<<2)

# special operator
#     identity operator

a = 5
b = 10
c = 5
print(a is c)

#     membership operator
# in 
a = [1,2,3,4,5,6]
print(5 in a)
print(15 not in a)