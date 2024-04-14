# 1. **Basics of Tuples:**
#    - Understanding what tuples are and their basic characteristics.
#    - Syntax for creating tuples.
#    - Immutable nature of tuples.

# A tuple in Python is a collection of elements enclosed within parentheses ().
# Tuples are similar to lists, but they are immutable, 
# meaning their elements cannot be changed after creation
# => Data integrity, Security

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with integers
int_tuple = (1, 2, 3, 4, 5)

# Creating a tuple with mixed data types
mixed_tuple = (1, 'a', 3.5, True)

# Creating a tuple with a single element
single_element_tuple = (42,)  # Note the comma after the element

# Creating a tuple with nested tuples
nested_tuple = ((1, 2), ('a', 'b'), (True, False))


# Attempting to change an element in a tuple
mixed_tuple = (1, 'a', 3.5, True)
mixed_tuple[0] = 10  # This will raise a TypeError because tuples are immutable



# 2. **Tuple Operations:**
#    - Accessing elements in a tuple using indexing and slicing.
#    - Concatenating tuples using the `+` operator.
#    - Multiplying tuples using the `*` operator.
#    - Finding the length of a tuple using the `len()` function.

# Example 1: Accessing elements in a tuple using indexing
my_tuple = ('a', 'b', 'c', 'd', 'e')

# Accessing the first element
print("First element:", my_tuple[0])

# Accessing the last element using negative indexing
print("Last element:", my_tuple[-1])


# Example 2: Slicing a tuple
my_tuple = ('a', 'b', 'c', 'd', 'e')

# Slicing from index 1 to 3 (exclusive)
print("Slice:", my_tuple[1:3])

# Slicing with a step size of 2
print("Every second element:", my_tuple[::2])



# Example 3: Concatenating tuples
tuple1 = ('a', 'b', 'c')
tuple2 = ('d', 'e', 'f')

# Concatenating two tuples
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)



# Example 4: Multiplying a tuple
my_tuple = ('a', 'b')

# Multiplying the tuple
multiplied_tuple = my_tuple * 3
print("Multiplied tuple:", multiplied_tuple)



# Example 5: Finding the length of a tuple
my_tuple = ('a', 'b', 'c', 'd', 'e')

# Finding the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)





# 3. **Tuple Methods:**
#    - `count()`: Counting occurrences of a specific element in a tuple.
#    - `index()`: Finding the index of the first occurrence of a specific element in a tuple.


# Example 1: Using the count() method
my_tuple = (1, 2, 3, 4, 2, 2, 5)

# Counting the number of occurrences of 2 in the tuple
count_of_2 = my_tuple.count(2)
print("Number of occurrences of 2:", count_of_2)

# Counting the number of occurrences of 6 (not in the tuple)
count_of_6 = my_tuple.count(6)
print("Number of occurrences of 6:", count_of_6)




# Example 2: Using the index() method
my_tuple = ('a', 'b', 'c', 'd', 'b')

# Finding the index of the first occurrence of 'b' in the tuple
index_of_b = my_tuple.index('b')
print("Index of 'b':", index_of_b)

# Finding the index of 'e' (not in the tuple)
try:
    index_of_e = my_tuple.index('e')
    print("Index of 'e':", index_of_e)
except ValueError:
    print("Element 'e' not found in the tuple.")



# 4. **Iterating Over Tuples:**
#    - Using loops (for loop) to iterate over elements in a tuple.
#    - Using tuple unpacking to assign values to multiple variables.


# Example 2: Tuple unpacking
my_tuple = (1, 2, 3)

# Unpacking the tuple into individual variables
a, b, c = my_tuple

# Printing the unpacked values
print("a:", a)
print("b:", b)
print("c:", c)



# Example 3: Iterating over elements in a tuple with indices
my_tuple = ('a', 'b', 'c', 'd')

# Iterating over the elements in the tuple with indices
for index, element in enumerate(my_tuple):
    print("Index:", index, "Element:", element)






# 5. **Nested Tuples:**
#    - Creating tuples of tuples.
#    - Accessing elements in nested tuples using multiple indexing.
    
# Example 2: Accessing elements in nested tuples
nested_tuple = ((1, 2), ('a', 'b'), (True, False))

# Accessing elements in nested tuples using multiple indexing
print("First element of the first tuple:", nested_tuple[0][0])
print("Second element of the second tuple:", nested_tuple[1][1])
print("Second element of the third tuple:", nested_tuple[2][1])



# 6. **Comparing Tuples:**
#    - Comparing tuples using comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
#    - Understanding the comparison rules for tuples.



# Example 1: Comparing tuples for equality and inequality
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6)

# Comparing tuples for equality
print("tuple1 == tuple2:", tuple1 == tuple2)  # True
print("tuple1 != tuple3:", tuple1 != tuple3)  # True


# Example 2: Comparing tuples lexicographically
tuple1 = ('a', 'b', 'c')
tuple2 = ('a', 'b', 'd')

# Comparing tuples lexicographically
print("tuple1 < tuple2:", tuple1 < tuple2)  # True (since 'c' < 'd')





# Example 3: Comparing tuples of different lengths
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 4)

# Comparing tuples of different lengths
print("tuple1 < tuple2:", tuple1 < tuple2)  # True (since both tuples are equal up to the length of tuple1)



# Example 4: Comparing tuples with mixed types
tuple1 = (1, 'a')
tuple2 = ('a', 1)

# Comparing tuples with mixed types
print("tuple1 < tuple2:", tuple1 < tuple2)  # True (since the first element of tuple1 is smaller in terms of type)



# 8. **Conversion to and from Tuples:**
#    - Converting other data structures (lists, strings) to tuples using the `tuple()` constructor.
#    - Converting tuples to other data structures (lists, strings) using appropriate methods.



# Example 1: Converting a list to a tuple
my_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(my_list)
print("Converted tuple:", converted_tuple)



# Example 2: Converting a string to a tuple
my_string = "hello"
converted_tuple = tuple(my_string)
print("Converted tuple:", converted_tuple)
# ('h', 'e', 'l', 'l', 'o')


# Example 3: Converting a tuple to a list
my_tuple = (1, 2, 3, 4, 5)
converted_list = list(my_tuple)
print("Converted list:", converted_list)



# Example 4: Converting a tuple to a string
my_tuple = ('a', 'b', 'c')
converted_string = ''.join(my_tuple)
print("Converted string:", converted_string)



# Example 5: Converting nested lists to nested tuples
nested_list = [[1, 2], [3, 4], [5, 6]]
converted_nested_tuple = tuple(tuple(inner_list) for inner_list in nested_list)
print("Converted nested tuple:", converted_nested_tuple)


# Example 6: Converting nested tuples to nested lists
nested_tuple = ((1, 2), (3, 4), (5, 6))
converted_nested_list = [list(inner_tuple) for inner_tuple in nested_tuple]
print("Converted nested list:", converted_nested_list)


# 9. **Tuple Packing and Unpacking:**
#    - Packing values into a tuple without explicitly creating a tuple.
#    - Unpacking tuples to assign values to multiple variables in a single line.

packed_tuple = 1,2,3
print(f"Packed Tuple", packed_tuple)  #Packed tuple: (1, 2, 3)



# Example 2: Unpacking a tuple to assign values
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print("a:", a)
print("b:", b)
print("c:", c)



# Example 3: Packing values of mixed data types
mixed_tuple = 'a', 1, True
print("Mixed tuple:", mixed_tuple)


# Example 4: Unpacking with the asterisk (*) operator
my_tuple = (1, 2, 3, 4, 5)
first, *rest, last = my_tuple
print("First element:", first)
print("Rest of the elements:", rest)
print("Last element:", last)


# Example 5: Unpacking values from nested tuples
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


# 10. **Use Cases and Best Practices:**
#     - Understanding when to use tuples instead of lists or other data structures.
#     - Best practices for using tuples effectively in Python code.


# ### Use Cases for Tuples:
# 1. **Immutable Data:** Tuples are immutable, making them suitable for storing data that should not be modified after creation, such as configuration settings, constants, or fixed-size collections.
# 2. **Efficient Packing:** Tuples can efficiently pack multiple values into a single variable, making them useful for returning multiple values from functions or representing fixed-size data structures.

# 3. **Hashability:** Tuples are hashable, meaning they can be used as keys in dictionaries or elements in sets. This makes tuples useful for data structures that require hashable elements.

# 4. **Ordered Collections:** Tuples maintain the order of elements, making them suitable for representing ordered data, such as coordinates, dates, or event records.

# ### Best Practices for Using Tuples:
# 1. **Use Tuples for Immutable Data:** Use tuples to store data that should not be modified after creation. This helps ensure data integrity and prevents accidental modifications.

# 2. **Use Tuple Unpacking for Multiple Assignments:** Take advantage of tuple unpacking to assign multiple values to variables in a single line, improving code readability and conciseness.

# 3. **Consider Named Tuples for Readability:** For tuples representing records or data structures with named fields, consider using named tuples from the `collections` module for improved readability and self-documenting code.

# 4. **Prefer Tuples for Heterogeneous Data:** Use tuples to store heterogeneous data (i.e., data of different types) when the order of elements is important and when individual elements have a semantic relationship.

# 5. **Document Tuple Structures:** When using tuples to represent structured data, document the meaning of each element or field in the tuple to improve code clarity and maintainability.

# 6. **Avoid Mutable Elements in Tuples:** Avoid including mutable objects such as lists or dictionaries as elements in tuples, as this can lead to unexpected behavior or unintended modifications.
