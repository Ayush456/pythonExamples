class Employee :
    empCount = 0;
    def __init__(self,at1,at2):
        self.at1 = at1;
        self.at2 = at2;
        Employee.empCount += 1



    def printEmployee(self):
        print("The First attribute : ",self.at1,"\t The second attribute : ",self.at2,"\t The count is : ", Employee.empCount )

print("Program starts here : \n")
obj1 = Employee("ayush","gupta")         # creating the first object of employee class
obj1.printEmployee();
obj2 = Employee("shyam","singh")         # creating the second object of employee class
obj2.printEmployee();


print("\n ",getattr(obj2,'at2'))         # accessing the attribute at2 of object2


setattr(obj1,'at3',50)      # adding third attribute in object1 which is 'at3'
print("\n The third attribute of object 1 is : ",obj1.at3)

delattr(obj1,'at3')                      # deleting the third attribute
print("Is there an attribute name 'at3' in object1 after deleting it? : " ,hasattr(obj1,'at3'))
