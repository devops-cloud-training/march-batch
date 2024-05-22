# fileops = open("mytext.txt","r")

# # content = fileops.read()
# print(fileops.readable())

# line1 = fileops.readline()
# line2 = fileops.readline()
# print(line1)
# print(line2)

# print(fileops.tell())
# # fileops.seek(0)

# content = fileops.readlines()
# print(content)


# fileops.close()

###################################

# with open("mytext.txt","r") as fileops:
#     content = fileops.readlines()
#     print(content)

# print("The file operation is over")

#########################################


fileops = open("newfile.txt","w+")

content = "Hey guys, how are you !"

fileops.write(content)

#fileops.close()


newcontent = "\nThis is new content"
fileops.write(newcontent)

fileops.seek(0)
print(fileops.readlines())


fileops.close()