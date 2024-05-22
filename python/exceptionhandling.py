
# name = "sathish"

# value = int(name)

# print(value)

try:
    # a = 10
    # b = 0
    # print(a/b)
    # sathish

    # abc = "hi"
    # print(int(abc))
    # a = [2,34,234,23,543,65,456]
    # print(a[10])
    print("this is try block")
except ZeroDivisionError:
    print("Hey please check if the number is divided by zero, because the logic is incorrect")
except NameError:
    print("some variable name you have used it improperly, please check it!")
except ValueError:
    print("Values are not used properly")
except:
    print("some other error")
finally:
    print("this is finally block")



a = 15
b= 10
c = a+b
print(c)

# a = 10
# b = 0
# print(a/b)

# print(dir(locals()["__builtins__"]))