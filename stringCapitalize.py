str = "this is a demo string"
print(str.capitalize())
print(str)
print(str.upper())
print(str.lower())
print(str.upper().center(50,"*"))

sub='i'
print("Counting the no of alphabets 'i' : ",str.count(sub))
sub2='string'
#whether the string will end with  "string"
print("",str.endswith(sub2))

#Does the string contains a word "demo"
sub3 = "demo"
sub4 = "technack"
print(str.__contains__(sub4))
 #finding the index of string "demo"
print("",str.find(sub3))

#replacing a string
print(str.replace("a","was"))



