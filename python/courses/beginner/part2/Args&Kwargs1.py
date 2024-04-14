
# 1
# Explanation:
# *args is a special syntax in Python used to pass a variable number of positional arguments to a function.
# It allows a function to accept any number of arguments without specifying them individually.
# The name args is just a convention; you can use any valid variable name preceded by *.
   
# def function_name(*args):
#     # Function body

# ex1
def summing(*args):
    total=0
    for number in args:
        total +=number
    
    return total

print(summing(23,11,45)) 
print(summing(1,2,3,4,5)) 



# ex2
def averageCalc(*args):
    if not args:
        return 0
    else:
        return sum(args)/len(args)
    
print(averageCalc(22,99,33,66))


# ex3. Keyword argument

def greeting(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print ("Hello, Guest")

greeting(name="Henriette")



#ex4.

def create_person(**kwargs):
    return kwargs

# Calling the function with different keyword arguments
person1 = create_person(name='Alice', age=30, city='New York')
person2 = create_person(name='Bob', age=25, city='Los Angeles')

print(person1)   # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person2)   # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}




# 2. **Function Definitions:**
#    - Learn how to define functions that accept `*args` and `**kwargs`.
#    - Understand how to use `*args` and `**kwargs` along with other parameters in a function definition.


# You can define functions that accept *args and **kwargs along
#  with other parameters in their signature. Here's how you can do it:


def function_name(arg1, arg2, *args, **kwargs):
    pass
    # Function body

def address_(name,*args,**kwargs):
    print(f"Address of : {name}")
    for arg in args:
        print(f"---{arg}\n")
    for key,value in kwargs.items():
        print(f"{key} : {value}")

address_("Peterson Ahmed","Los Angeles","New York",state="Ohio",age=23)

# 3. **Unpacking:**
#    - Learn about unpacking argument lists and dictionaries using `*` and `**` operators.
#    - Understand how to pass elements of a list as separate arguments to a function using `*`.

# Unpacking in Python refers to the process of extracting elements from iterables like lists or 
# dictionaries and passing them as separate arguments to a function. 

# The * operator is used to unpack iterables like lists, tuples, or strings into separate elements.
# The ** operator is used to unpack dictionaries into separate key-value pairs.


def greet (name,age):
    print(f"Hello, {name}! You are {age} years old")


person = ["Peterson",23]
greet(*person)  #Hello, Peterson! You are 23 years old


#ex

def introduce(name,city):
    return f"Welcome {name} in the city of {city} "

person = {
    "name":"Alice Bob",
    "city":"Las ve Gas"
}

print(introduce(**person))

# Welcome Alice Bob in the city of Las ve Gas 


# ex
# Unpackin the Strings

def capitalize_(first,second):
    print(f"{first.capitalize()} { second.capitalize()}")


names = "noah harari"
capitalize_(*names.split())
# Noah Harari



# ex

def calculate_total(a, b, c):
    return a + b + c

values = (10, 20, 30)
total = calculate_total(*values)  # Unpacking the tuple and passing its elements as separate arguments
print("Total:", total)  # Output: Total: 60


# ex

def multiplication(a,b,c):
    return a*b*c


nested_values = [[2,3,4],[9,5,6],[5,6,2]]
result = [multiplication(*nested) for nested in nested_values]
print(result)  #[24, 270, 60]



# 4. **Use Cases:**
#    - Explore various use cases for `*args` and `**kwargs`:
#      - Passing a variable number of arguments to a function.
#      - Implementing decorators that accept arbitrary arguments.
#      - Writing wrapper functions that pass arguments to another function dynamically.
#      - Calling functions with variable argument lists based on conditions.


def perform_operation(operation, *args):
    if operation == 'sum':
        return sum(args)
    elif operation == 'product':
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return None

print(perform_operation('sum', 1, 2, 3))       # Output: 6
print(perform_operation('product', 2, 3, 4))   # Output: 24
print(perform_operation('average', 1, 2, 3))   # Output: None


# 5. **Advanced Topics:**
#    - Explore advanced topics such as combining `*args` and `**kwargs` with default arguments, type hints, and function annotations.
#    - Learn about the `inspect` module for working with function signatures dynamically.

def example_function(a, b=10, *args, **kwargs):
    """
    Example function with default arguments, *args, and **kwargs.
    
    Args:
        a (int): Required positional argument.
        b (int, optional): Optional positional argument with default value 10.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
        
    Returns:
        None
    """
    print("a:", a)
    print("b:", b)
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

# Function call with all arguments
example_function(1, 2, 3, 4, c=5, d=6)


# Type Hints and Function Annotations:

def intro(name:str,age:int)->str:
    return f"Hello, {name}. You are {age} years old."

student={
    "name":"Peter",
    "age":34
}
print(intro(**student))


# 6. **Examples and Practice:**
#    - Practice writing functions that utilize `*args` and `**kwargs` in various scenarios.
#    - Study existing codebases to see how `*args` and `**kwargs` are used in real-world applications.

