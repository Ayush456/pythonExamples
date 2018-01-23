
def AssertionFunction(temperature):
    assert (temperature < 0),"Its too cold"
    return temperature+27

# Assertion will happen when the condition is not true
print("Output without assertion : ")
AssertionFunction(-5)


#print("\n Output with assertionError")
#AssertionFunction(5)