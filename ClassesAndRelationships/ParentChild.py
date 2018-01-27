class Parent :

    def __init__(self):
        print("Calling the parent constructor")

    def parentMethod(self):
        print("Calling the parent method")



class Child :

    def __init__(self):
        print("You are in the child constructor")

    def childMethod(self):
        print("You are in the child method")





parent = Parent()
parent.parentMethod()

child = Child()
child.childMethod()
