
class UserException( Exception ):
    def __init__(self,var):
        self.var = var

try:
    value = int(input("enter a number : "))
    if value < 10 :
        raise UserException("this is my exception")
except UserException as e:
    print("Throwing an Exception",e.var)

