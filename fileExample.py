

filename = open("support.py","r+")
print("Name of the file is : ",filename.name)
print("Mode of operation is : ",filename.mode)

#for index in range(len(filename)):
 #    line =
count = 0
for index in filename :
    #line = next(filename)
    count = count + 1

print("The no of lines is : ",count)
