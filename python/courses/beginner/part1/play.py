from functools import reduce
chars = ['Hello','Message','from','python']
message=reduce(lambda str1,str2: str1 + " " + str2,chars)
print(message)