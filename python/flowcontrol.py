import datetime

# If else conditions 
# a = 20
# b = 10
# c = a-b

# print(a)
# print(b)
# print(c)

# print("The value is Zero")
# print("The value is positive")
# print("The value is negative")

# if c == 0:
#     print("The value is Zero")
# elif c > 0:
#     print("The value is positive")
#     print("this is additional line")
#     if c > 10:
#         print("the number is greater than 10")
#     elif c < 10:
#         print("The number is less than 10")
#     else:
#         print("the number is equals to 10")
# else:
#     print("The value is negative")

# print("this is new line")

# looping - for , while

# sequences = [1,2,3,4,5,6,7,8,9,324,43,25,345,34,23,4,234,423,5,43,6,45,43,5,23]

# for mynum in sequences:
#     if mynum == 4:
#         print(mynum)
    
# print only the numbers which are divided by 2
# print only the odd numbers
# print only the prime numbers
# print all the alternate numbers
# print if the number is even but not divisible by 8
# print if the number is divisible by 5 and its quotient as well

# timenow1 = datetime.datetime.now()
# # print(timenow)

# for num in range(1,10000):
#     if num %10 == 0:
#         # pass
#         print("first",num)

# timenow2 = datetime.datetime.now()
# # print(timenow)
# # value = "Sathish is a trainer"

# # for character in value:
# #     print(character)

# timenow3 = datetime.datetime.now()
# # print(timenow)

# i = 0
# while i < 10000:
#     print(i)
#     i += 10 # i = i+1

# timenow4 = datetime.datetime.now()

# print(timenow1)
# print(timenow2)
# print(timenow3)
# print(timenow4)


for i in range(1,100):
    
    if i % 5 == 0:
        break
    print(i)

print("Loop ended")