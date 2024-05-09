# numeric 
#int
#float
#complex
# decimal, hexa decimal, octal, binary
# a = 5
# print(type(a))
# b = 24.5
# print(type(b))
# c = 4+2j
# print(type(c))

# d = 0b101111
# print(d)
# print(type(d))

# e = 0o10324511
# print(e)
# print(type(e))

# d = 0xFD11
# print(d)
# print(type(d))


# string
# bool


# lists  -are mutable

# fruits = ["apple", "orange", "grapes", "banana", "litchi"]
# sequences = [1,2,3,4,5,6,7,8,9]
# myownvalues = ["sathish","abc",2,3,4,5,6,"xyz"]

# print(len(fruits))
# fruits.append("pomo")
# print(fruits)
# fruits.insert(1,"mango")
# print(fruits)
# fruits.remove("orange")
# print(fruits)

# myownvalues.extend(fruits)
# print(myownvalues)
# fruits.reverse()
# print(fruits)

# myownvalues.sort()
# print(myownvalues)

# tuples
# sets
# dictionary

# sequences = (1,2,3,4,5,6,7,8,9,2,3,4,3,3,43,3,2)
# print(len(sequences))
# print(sequences.count(3))
# print(sequences[::-1])

# Sets

myset = {1,2,3,4,5,6,7,8,9,6,5,6,4,5,6,7,4,3,5,6,3,2,2,4,3,5,6,7,8,9,7,6,5,4,3}

newset = {4,5,7,8,432,24,23,1,4,323,54,65,76}

print(type(myset))

# myset.add(12)
# myset.add(1322)
# myset.add(1422)
# myset.discard(6)

# print(myset.union(newset))
# print(myset.intersection(newset))
# print(myset.difference(newset))

# print(myset)

#dict

employee = {
    "name" : "sathish",
    "hobbies": ["music","cricket","football","cooking"],
    "age" : 90,
    "salary": 9000000000,
    "IsMarried": True,
    "city" : "Chennai"
}

eatables = {
    "fruits": ["apple","orange","banana"],
    "veggies": "capsicum",
    "sweet" : ["kesari","laddu"]
}

print(type(employee))

emptyset = set()

print(type(emptyset))
print(emptyset)

emptyset.add(3)
print(emptyset)
