# # What are Lists?
# Lists are one of the most versatile and commonly used data structures in Python.
# A list is a collection of elements, where each element can be of any data type (e.g., integers, floats, strings, or even other lists).
# Lists are ordered, mutable (modifiable), and can contain duplicate elements.
# Lists are defined using square brackets [ ] and elements are separated by commas.

# Why Use Lists?
# Lists provide a convenient way to store and manipulate collections of data.
# They allow for flexible storage and retrieval of elements.
# Lists support a wide range of operations, such as adding, removing, and modifying elements.
# Lists are used in a variety of applications, including data processing, algorithm development, and building complex data structures.

#  Creating Lists  
#Accessing Elements in a List List 
#Indexing and Slicing
numbers=[1,2,3,4,5]
fruits=["apple","banana","cherry"]
mixed=[1,2,"apple",3.14,True]

cars=["Toyota","Honda","Ford","Chevrolet","Nissan","BMW"]

print(fruits[-1]) # cherry
print(len(numbers)) # 5
print(cars[3:]) # ['Chevrolet', 'Nissan', 'BMW']
print(cars[:3]) # ['Toyota', 'Honda', 'Ford']

print(cars[1:4]) # ['Honda', 'Ford', 'Chevrolet']
print(numbers[::-1]) # [5, 4, 3, 2, 1]

print(numbers.count(3)) # 1


#lists methods

# Define a list
numbers = [1, 2, 3, 4, 5]

# Append method - adds an element to the end of the list
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Extend method - extends the list by appending elements from another iterable
numbers.extend([7, 8, 9])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert method - inserts an element at a specified position
numbers.insert(0, 0)
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove method - removes the first occurrence of a specified value
numbers.remove(5)
print(numbers)  # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9]

# Pop method - removes and returns the element at a specified index (or the last element if index is not provided)
popped_element = numbers.pop(0)
print(popped_element)  # Output: 0
print(numbers)  # Output: [1, 2, 3, 4, 6, 7, 8, 9]

# Index method - returns the index of the first occurrence of a specified value
index_of_6 = numbers.index(6)
print(index_of_6)  # Output: 4

# Count method - returns the number of occurrences of a specified value
count_of_6 = numbers.count(6)
print(count_of_6)  # Output: 1

# Sort method - sorts the list in ascending order (in-place)
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 6, 7, 8, 9]

# Reverse method - reverses the elements of the list (in-place)
numbers.reverse()
print(numbers)  # Output: [9, 8, 7, 6, 4, 3, 2, 1]

# Copy method - returns a shallow copy of the list
numbers_copy = numbers.copy()
print(numbers_copy)  # Output: [9, 8, 7, 6, 4, 3, 2, 1]



# Define a list
numbers = [1, 2, 3, 4, 5]

# Modifying Elements in a List
numbers[0] = 10
print(numbers)  # Output: [10, 2, 3, 4, 5]

# Adding Elements to a List
numbers.append(6)
print(numbers)  # Output: [10, 2, 3, 4, 5, 6]

# Removing Elements from a List
numbers.remove(3)
print(numbers)  # Output: [10, 2, 4, 5, 6]

# Checking Membership in a List
is_present = 5 in numbers
print(is_present)  # Output: True

# List Concatenation and Repetition
letters = ['a', 'b', 'c']
concatenated_list = numbers + letters
print(concatenated_list)  # Output: [10, 2, 4, 5, 6, 'a', 'b', 'c']

repeated_list = letters * 2
print(repeated_list)  # Output: ['a', 'b', 'c', 'a', 'b', 'c']

# List Length and Counting Elements
list_length = len(numbers)
print(list_length)  # Output: 5

count_of_2 = numbers.count(2)
print(count_of_2)  # Output: 1


# Example 1: List Comprehension for Strings
# Given a list of strings, create a new list with the lengths of each string

# Original list of strings
words = ['apple', 'banana', 'cherry', 'orange']

# Using list comprehension to create a new list with lengths of strings
word_lengths = [len(word) for word in words]

# Print the original list and the new list with string lengths
print("Original list:", words)
print("List with string lengths:", word_lengths)

# Output:
# Original list: ['apple', 'banana', 'cherry', 'orange']
# List with string lengths: [5, 6, 6, 6]



# Example 2: List Comprehension for File Handling
# Given a list of filenames, create a new list containing the contents of each file

# Original list of filenames
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# Using list comprehension to read contents of each file and create a new list
file_contents = [open(file).read() for file in file_names]

# Print the original list of filenames and the new list with file contents
print("Original list of filenames:", file_names)
print("List with file contents:", file_contents)

# Output:
# Original list of filenames: ['file1.txt', 'file2.txt', 'file3.txt']
# List with file contents: ['Contents of file1.txt', 'Contents of file2.txt', 'Contents of file3.txt']



# Example 3: List Comprehension with Conditions
# Given a list of numbers, create a new list containing only the even numbers

# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension with a condition to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the original list and the new list with even numbers
print("Original list:", numbers)
print("List with even numbers:", even_numbers)

# Output:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List with even numbers: [2, 4, 6, 8, 10]




# Example 2: Looping Through Lists with List Comprehensions
# Given a list of strings, create a new list with uppercase versions of each string

# Original list of strings
words = ['apple', 'banana', 'cherry']

# Using a list comprehension to create a new list with uppercase strings
uppercase_words = [word.upper() for word in words]

# Print the original list and the new list with uppercase strings
print("Original list:", words)
print("List with uppercase strings:", uppercase_words)

# Output:
# Original list: ['apple', 'banana', 'cherry']
# List with uppercase strings: ['APPLE', 'BANANA', 'CHERRY']





# Example 3: Using enumerate() Function with Lists
# Given a list of names, print each name along with its index

# Original list of names
names = ['Alice', 'Bob', 'Charlie', 'David']

# Using the enumerate() function to iterate over the list and print each name with its index
print("Using enumerate():")
for index, name in enumerate(names):
    print(f"Index {index}: {name}")

# Output:
# Using enumerate():
# Index 0: Alice
# Index 1: Bob
# Index 2: Charlie
# Index 3: David






#enumerate() is a built-in Python function used to iterate over
# a sequence (such as a list, tuple, or string) while keeping track of the index of each item.
# It returns an enumerate object, which yields pairs of index and value for each item in the sequence.

#syntax:  enumerate(iterable, start=0)
#iterable: The sequence to be iterated over.
#start (optional): The index to start counting from. By default, it is 0.

""" 

#### Iterating Over Lists
1. Using for Loops with Lists
2. Looping Through Lists with List Comprehensions
3. Using enumerate() Function with Lists
4. Looping Over Multiple Lists Simultaneously

#### Common List Patterns and Techniques
1. Finding Maximum and Minimum Values in a List
2. Checking for Duplicates in a List
3. Flattening Nested Lists
4. List Reversal
5. List Unpacking
6. Zip and Unzip Lists

#### Advanced List Topics
1. List Mutability vs. Immutability
2. Deep Copy vs. Shallow Copy
3. List Memory Management
4. Using Lists in Functional Programming
5. List Performance and Efficiency Considerations

#### Practical Applications and Exercises
1. Building a To-Do List Application
2. Implementing a Simple Database with Lists
3. Solving Coding Challenges with Lists
5. Implementing Lists in Real-world Projects

#### Conclusion
1. Summary of Key Concepts
2. Next Steps in Mastering Lists
3. Further Resources and References

 """