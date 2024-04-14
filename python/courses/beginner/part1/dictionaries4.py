# 1. Introduction to Dictionaries

# What are dictionaries?
# - Dictionaries are a built-in data type in Python used to store key-value pairs.
# - Each element in a dictionary consists of a key and its corresponding value.
# - Keys are unique and immutable, while values can be of any data type (e.g., integers, strings, lists, other dictionaries).

# Why use dictionaries?
# - Dictionaries provide a flexible way to organize and manage data.
# - They offer efficient lookups based on keys, making it easy to retrieve values associated with specific keys.
# - Dictionaries are commonly used in scenarios where data needs to be accessed and manipulated based on unique identifiers (keys).

# Basic syntax for creating dictionaries.
# - Dictionaries are created using curly braces { }.
# - Each key-value pair is separated by a colon :, and pairs are separated by commas.
# - Syntax: {key1: value1, key2: value2, ...}

# Characteristics of dictionaries
# - Unordered: The elements in a dictionary are not ordered or indexed. The order of elements is not guaranteed.
# - Mutable: Dictionaries can be modified after creation. You can add, remove, or modify key-value pairs.
# - Can contain any data type: Both keys and values in a dictionary can be of any data type.
#   For example, keys can be integers, strings, or tuples, while values can be integers, strings, lists, or even other dictionaries.

# Example of creating a dictionary
# Syntax: {key1: value1, key2: value2, ...}
student = {'name': 'Alice', 'age': 25, 'grade': 'A'}







# 2. Accessing and Modifying Dictionary Elements

# Accessing values using keys
# - You can access the value associated with a key in a dictionary using square brackets [] or the get() method.
# - If the key exists, the corresponding value is returned; otherwise, an error (KeyError) is raised with square brackets,
#   or None is returned with the get() method.

# Example 1: Accessing values using square brackets
student = {'name': 'Alice', 'age': 25, 'grade': 'A'}
print(student['name'])  # Output: Alice

# Example 2: Accessing values using the get() method
print(student.get('age'))  # Output: 25

# Modifying values in dictionaries
# - You can modify the value associated with a key in a dictionary by assigning a new value to that key.

# Example: Modifying a value in the dictionary
student['grade'] = 'B'
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'B'}

# Adding key-value pairs
# - You can add new key-value pairs to a dictionary by assigning a value to a new key.

# Example: Adding a new key-value pair to the dictionary
student['major'] = 'Computer Science'
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'B', 'major': 'Computer Science'}

# Removing key-value pairs
# - You can remove a key-value pair from a dictionary using the del statement, the pop() method,
#   the popitem() method, or the clear() method.

# Example 1: Removing a key-value pair using del statement
del student['age']
print(student)  # Output: {'name': 'Alice', 'grade': 'B', 'major': 'Computer Science'}

# Example 2: Removing a key-value pair using pop() method
grade = student.pop('grade')
print(grade)    # Output: B
print(student)  # Output: {'name': 'Alice', 'major': 'Computer Science'}

# Example 3: Removing the last key-value pair using popitem() method
last_item = student.popitem()
print(last_item)  # Output: ('major', 'Computer Science')
print(student)    # Output: {'name': 'Alice'}

# Example 4: Clearing all key-value pairs using clear() method
student.clear()
print(student)  # Output: {}








# 3. Dictionary Methods

# Overview of common dictionary methods
# - Python dictionaries provide several built-in methods for performing various operations on dictionaries.
# - Here's an overview of some common dictionary methods:
#   - keys(): Returns a view object containing the keys of the dictionary.
#   - values(): Returns a view object containing the values of the dictionary.
#   - items(): Returns a view object containing the key-value pairs of the dictionary as tuples.
#   - get(key): Returns the value associated with the specified key, or None if the key is not found.
#   - update(other_dict): Updates the dictionary with key-value pairs from another dictionary or iterable.
#   - pop(key): Removes the key-value pair with the specified key and returns the corresponding value.
#   - popitem(): Removes and returns the last key-value pair as a tuple.
#   - clear(): Removes all key-value pairs from the dictionary.

# Example: Overview of common dictionary methods
student = {'name': 'Alice', 'age': 25, 'grade': 'A'}

# keys() method
print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])

# values() method
print(student.values())  # Output: dict_values(['Alice', 25, 'A'])

# items() method
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('grade', 'A')])

# get() method
print(student.get('name'))  # Output: Alice

# update() method
student.update({'major': 'Computer Science'})
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

# pop() method
grade = student.pop('grade')
print(grade)    # Output: A
print(student)  # Output: {'name': 'Alice', 'age': 25, 'major': 'Computer Science'}

# popitem() method
last_item = student.popitem()
print(last_item)  # Output: ('major', 'Computer Science')
print(student)    # Output: {'name': 'Alice', 'age': 25}

# clear() method
student.clear()
print(student)  # Output: {}






# 4. Dictionary Comprehensions

# Syntax for dictionary comprehensions
# - Dictionary comprehensions provide a concise way to create dictionaries in Python using a single line of code.
# - Syntax: {key_expression: value_expression for item in iterable}

# Example 1: Creating a dictionary of squares using a for loop
squares = {}
for num in range(1, 6):
    squares[num] = num ** 2
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Creating the same dictionary using dictionary comprehension
squares = {num: num ** 2 for num in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Examples of dictionary comprehensions in practical scenarios

# Example 3: Creating a dictionary with uppercase keys from a list of strings
names = ['alice', 'bob', 'charlie']
uppercase_names = {name.upper(): name for name in names}
print(uppercase_names)  # Output: {'ALICE': 'alice', 'BOB': 'bob', 'CHARLIE': 'charlie'}

# Example 4: Creating a dictionary with lengths of strings as keys and corresponding strings as values
words = ['apple', 'banana', 'cherry']
word_lengths = {len(word): word for word in words}
print(word_lengths)  # Output: {5: 'apple', 6: 'banana', 5: 'cherry'} (Note: Duplicates are not allowed for keys)

# Example 5: Filtering dictionary items based on a condition
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
passed_students = {name: score for name, score in student_scores.items() if score >= 90}
print(passed_students)  # Output: {'Bob': 92, 'David': 95}






# 5. Nested Dictionaries

# Creating and working with nested dictionaries
# - Nested dictionaries are dictionaries that contain other dictionaries as values.
# - They are useful for representing hierarchical data structures or organizing data with multiple levels of abstraction.

# Example: Creating a nested dictionary to represent student information
student_info = {
    'Alice': {'age': 25, 'major': 'Computer Science'},
    'Bob': {'age': 23, 'major': 'Engineering'},
    'Charlie': {'age': 22, 'major': 'Mathematics'}
}

# Accessing and modifying values in nested dictionaries
# - You can access and modify values in nested dictionaries using multiple square brackets [] or chaining.
# - To access or modify a value in a nested dictionary, you need to specify the keys at each level of nesting.

# Example 1: Accessing values in nested dictionaries
print(student_info['Alice']['age'])  # Output: 25

# Example 2: Modifying values in nested dictionaries
student_info['Alice']['age'] = 26
print(student_info['Alice']['age'])  # Output: 26

# Iterating over nested dictionaries
# - You can iterate over nested dictionaries using nested loops or dictionary methods like items().

# Example: Iterating over nested dictionaries using nested loops
for name, info in student_info.items():
    print(f"Student: {name}")
    for key, value in info.items():
        print(f"{key}: {value}")

# Output:
# Student: Alice
# age: 26
# major: Computer Science
# Student: Bob
# age: 23
# major: Engineering
# Student: Charlie
# age: 22
# major: Mathematics





# 6. Using Dictionaries in Loops

# Iterating over keys, values, and key-value pairs
# - You can iterate over keys, values, or key-value pairs (items) of a dictionary using different techniques.

# Example 1: Iterating over keys
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
for name in student_scores.keys():
    print(name)

# Example 2: Iterating over values
for score in student_scores.values():
    print(score)

# Example 3: Iterating over key-value pairs using items()
for name, score in student_scores.items():
    print(f"{name}: {score}")

# Techniques for looping through dictionaries efficiently
# - When iterating over dictionaries, consider using methods like keys(), values(), or items() based on the specific requirement.
# - If you only need to access keys or values, using keys() or values() directly can be more efficient than using items().

# Example: Looping through keys and accessing values
for name in student_scores.keys():
    score = student_scores[name]
    print(f"{name}: {score}")

# Example: Looping through values and accessing keys
for score in student_scores.values():
    name = next(key for key, value in student_scores.items() if value == score)
    print(f"{name}: {score}")




# 7. Dictionary Views

# Understanding dictionary views
# - Dictionary views are dynamic objects that provide a view of the keys, values, or key-value pairs of a dictionary.
# - There are three types of dictionary views:
#   - keys(): Provides a view of the keys in the dictionary.
#   - values(): Provides a view of the values in the dictionary.
#   - items(): Provides a view of the key-value pairs (tuples) in the dictionary.

# Example: Creating a dictionary
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Example 1: Dictionary view of keys
keys_view = student_scores.keys()
print(keys_view)  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])

# Example 2: Dictionary view of values
values_view = student_scores.values()
print(values_view)  # Output: dict_values([85, 92, 78])

# Example 3: Dictionary view of items
items_view = student_scores.items()
print(items_view)  # Output: dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78)])

# Advantages and use cases of dictionary views
# - Dictionary views provide a dynamic and memory-efficient way to interact with dictionary contents.
# - They reflect changes made to the underlying dictionary in real-time, making them suitable for scenarios where the dictionary is frequently updated.
# - Dictionary views can be useful for tasks like filtering, mapping, or performing set operations on dictionary contents without creating intermediate lists.




   
# 8. Sorting Dictionaries

# Sorting dictionaries by keys or values
# - Python provides built-in functions and methods for sorting dictionaries by keys or values.

# Example 1: Sorting dictionary by keys
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
sorted_by_keys = sorted(student_scores.items())  # Sort by keys (default behavior)
print(sorted_by_keys)  # Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Example 2: Sorting dictionary by values
sorted_by_values = sorted(student_scores.items(), key=lambda x: x[1])  # Sort by values
print(sorted_by_values)  # Output: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Custom sorting criteria for dictionaries
# - You can define custom sorting criteria using a key function for more complex sorting requirements.

# Example 3: Sorting dictionary by keys in descending order
sorted_by_keys_desc = sorted(student_scores.items(), key=lambda x: x[0], reverse=True)  # Sort by keys in descending order
print(sorted_by_keys_desc)  # Output: [('Charlie', 78), ('Bob', 92), ('Alice', 85)]




   
# 9. Merging and Updating Dictionaries

# Techniques for merging dictionaries
# - Python provides several techniques for merging dictionaries, including the update() method and dictionary unpacking.

# Example 1: Using update() method to merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Example 2: Using dictionary unpacking to merge dictionaries
dict3 = {'d': 5, 'e': 6}
merged_dict = {**dict1, **dict3}
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}

# Handling conflicts and duplicates when merging dictionaries
# - When merging dictionaries, conflicts may arise if keys are duplicated between dictionaries.
# - The update() method overwrites values for existing keys, while dictionary unpacking retains the values of the first occurrence of each key.

# Example 3: Handling conflicts with update() method
dict4 = {'b': 7, 'c': 8}
dict1.update(dict4)
print(dict1)  # Output: {'a': 1, 'b': 7, 'c': 8}

# Example 4: Handling conflicts with dictionary unpacking
dict5 = {'b': 9, 'c': 10}
merged_dict_conflict = {**dict1, **dict5}
print(merged_dict_conflict)  # Output: {'a': 1, 'b': 7, 'c': 10, 'd': 5, 'e': 6}


#merge two lists into dictionary
countries =["Rwanda","Cameroon","England"]

cities=["Kigali","Yaounde","London"]

if len(countries) == len(cities):
    dict1={countries[i]:cities[i] for i in range(len(cities))}
    
else:
    print("Your lists are not of equal length")


# OR

contrY_city= {
   country:city for country,city in zip(countries,cities)
}

print(contrY_city)

# 10. Working with Default Values

# Using setdefault() and get() methods to handle missing keys
# - Python provides setdefault() and get() methods to handle missing keys in dictionaries and customize default values.

# Example 1: Using setdefault() method to handle missing keys
student_scores = {'Alice': 85, 'Bob': 92}
# If 'Charlie' key is missing, set its value to 0
student_scores.setdefault('Charlie', 0)
print(student_scores)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 0}

# Example 2: Using get() method to handle missing keys
# If 'David' key is missing, return the default value of -1
score_david = student_scores.get('David', -1)
print(score_david)  # Output: -1

# Customizing default values for dictionaries
# - You can customize default values returned for missing keys by passing a default value to setdefault() or get() methods.

# Example 3: Customizing default values for missing keys
# If 'Eve' key is missing, return the default value of 'Not Found'
score_eve = student_scores.get('Eve', 'Not Found')
print(score_eve)  # Output: Not Found





# 11. Dictionary Operations and Efficiency

# Understanding time complexity of dictionary operations
# - Dictionary operations in Python typically have an average time complexity of O(1) for accessing, inserting, updating, and deleting elements.
# - This means that the time taken to perform these operations does not depend on the size of the dictionary.

# Example 1: Time complexity of dictionary operations
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
# Accessing a value by key
alice_score = student_scores['Alice']  # O(1)
# Inserting a new key-value pair
student_scores['David'] = 90  # O(1)
# Updating an existing value
student_scores['Alice'] = 88  # O(1)
# Deleting a key-value pair
del student_scores['Charlie']  # O(1)

# Best practices for optimizing dictionary usage
# - Use dictionary comprehension or the dict() constructor for creating dictionaries efficiently.
# - Prefer built-in methods like keys(), values(), and items() for iterating over dictionary keys, values, and key-value pairs, respectively.
# - Avoid unnecessary copying of dictionaries; prefer in-place modification whenever possible.
# - Be mindful of memory usage when working with large dictionaries; consider using data structures like defaultdict or Counter for specialized use cases.

# Example 2: Using dictionary comprehension for efficient creation
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
student_scores = {name: score for name, score in zip(names, scores)}  # Efficient creation using comprehension
print(student_scores)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}





