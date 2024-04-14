def intro(name:str,age:int)->str:
    return f"Hello, {name}. You are {age} years old."

student={
    "name":"Peter",
    "age":34
}
print(intro(**student))