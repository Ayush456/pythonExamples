

filename = open("support.py","r+")
print("Name of the file is : ",filename.name)
print("Mode of operation is : ",filename.mode)

#for index in range(len(filename)):
 #    line =
count = 0
start=filename.tell()
print("Start of file : ",start)
for index in filename :
    #line = next(filename)
    count = count + 1

str = "#End of the file"
print("The no of lines is : ",count)
print("EOF : ",filename.tell())





