from ImportModules import funct1  # you are importing only funct1 from module ImportModule.py

print("Please Enter your Name : ")
name = input();

funct1(name)
funct2(name) # ypu are calling funct2 which is not imported hence an error
