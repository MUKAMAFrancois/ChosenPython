#Lambda functions


# example 1. Filter====
numbers = [12,23,45,68,90]
evens = filter(lambda num : num%2 ==0, numbers)
print(list(evens))


# The filter() function. It takes two parameters: a function and an iterable. 
# The function is applied to each element of the iterable, # and only the elements 
# for which the function returns True are included in the output.

# filter(function, iterable)



#example 2. map

squares = map(lambda num: num**2, numbers)
print(f"Squares: \n {list(squares)}")

# With map. it can take more than one iterable
# The function is applied to each element of the iterables,
# and the results are collected in a list.
# map(function, iterable1, iterable2, ...)

first_names = ['peter','sandrine','enoch']
lat_names = ['John','Alia','James']

capitalized = map(lambda names:(names[0].capitalize(),names[1].capitalize()),zip(first_names,lat_names))
print(list(capitalized))



# example 3....

multiply = lambda x,y,z : x*y*z
print(multiply(2,3,4))


# Ex 4. sort list of tuples

students =[
    ('Herman',34), ('Joseph',56),('Peter',9),('Victor',23)
]

students.sort(key=lambda input: input[1],reverse=True)

print(students)  #[('Joseph', 56), ('Herman', 34), ('Victor', 23), ('Peter', 9)]


# Ex 5. Sort the string based on length

countries = ['United States','Canada','Philipines','Australia','Spain','Vatican City','Bangladesh']
countries.sort(key=lambda y : len(y))
print(countries) 
# ['Spain', 'Canada', 'Australia', 'Philipines', 'Bangladesh', 'Vatican City', 'United States']


# sorted!!!!!!!!!!!!! sorted(iterable, key=None, reverse=False)


# sorted is indeed a built-in function in Python. 
# It is used to sort iterables such as lists, tuples, and dictionaries.
# Unlike the sort() method, which sorts a list in place, the sorted()
# function returns a new sorted list and does not modify the original list.

numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 5, 8]




def sorting(list_obj):
    sorted_list=[]
    for item in sorted(list_obj,key=len):
        sorted_list.append(item)

    return sorted_list

countries = ['United States','Canada','Philipines','Australia','Spain','Vatican City','Bangladesh']
print(sorting(countries))



#Ex 6. Closures


def powering(exponent):
    return lambda number: number ** exponent

sq= powering(2)
print(sq(30))  #900

cube = powering(3)
print(cube(20))  #8000


def addNumber(added):
    return lambda original: original + added

add5 = addNumber(5)
incremented = add5(12) # 17



#ex 7. reduce() with lambdas


# The reduce() function in Python is used to apply a rolling computation
# to sequential pairs of values in an iterable, ultimately 
# reducing the iterable to a single value. 
# It's part of the functools module in Python 3 and above, 
# so you need to import it before using it.


# from functools import reduce

# result = reduce(function, iterable[, initial])


# function: The function to apply to each pair of elements. It should take two arguments and return a single value.
# iterable: The iterable (e.g., list, tuple) to be reduced.
# initial (optional): An optional initial value. 
# If provided, it's used as the first argument to the function when reducing the iterable.
# If not provided, the first two elements of the iterable are used as initial values.



from functools import reduce


marks = [56,89,99,233,56]
total = reduce(lambda x,y : x+y,marks)
print(total) #533


product = reduce(lambda x,y: x*y,marks,1)
print(product) #6438091968

chars = ['Hello','Message','from','python']
message=reduce(lambda str1,str2: str1 + " " + str2,chars)
print(message)  # Hello Message from python