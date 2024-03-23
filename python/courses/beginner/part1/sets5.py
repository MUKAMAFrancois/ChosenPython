# Introduction to Sets

# What are sets?
# - Sets in Python are an unordered collection of unique elements.
# - Unlike lists or tuples, sets do not maintain any specific order for their elements.
# - Sets are mutable, meaning their elements can be added, removed, or modified after creation.
# - Sets cannot contain duplicate elements; each element in a set is unique.

# Basic syntax for creating sets
# - Sets are created using curly braces {} or the set() constructor.
# - Elements are separated by commas within the braces.
# - If duplicate elements are provided during set creation, they are automatically removed to maintain uniqueness.

# Example 1: Creating a set using curly braces
fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Example 2: Creating a set using the set() constructor
colors = set(['red', 'green', 'blue'])
print(colors)  # Output: {'red', 'green', 'blue'}

# Example 3: Creating a set with duplicate elements
numbers = {1, 2, 3, 3, 4, 5, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5} (Duplicate elements are automatically removed)






# Set Operations

# Example 1: Adding elements to a set using the add() method
colors = {'red', 'green', 'blue'}
colors.add('yellow')
print(colors)  # Output: {'red', 'green', 'blue', 'yellow'}

# Example 2: Removing elements from a set using the remove() method
colors.remove('green')
print(colors)  # Output: {'red', 'blue', 'yellow'}

# Example 3: Checking membership in a set using the in keyword
if 'red' in colors:
    print("Red color is present")  # Output: Red color is present

# Example 4: Set operations: union, intersection, difference, symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: Elements present in either set1 or set2
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements present in both set1 and set2
intersection_set = set1 & set2
print(intersection_set)  # Output: {3, 4}

# Difference: Elements present in set1 but not in set2
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Symmetric Difference: Elements present in either set1 or set2, but not both
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}






# Iterating Over Sets

# Example 1: Using a for loop to iterate over elements in a set
fruits = {'apple', 'banana', 'cherry'}
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry (order may vary)

# Example 2: Set comprehensions for concise creation of sets
numbers = {1, 2, 3, 4, 5}
squared_numbers = {x ** 2 for x in numbers}
print(squared_numbers)  # Output: {1, 4, 9, 16, 25}

# Example 3: Using a for loop with conditional statements to filter elements in a set
names = {'Alice', 'Bob', 'Charlie', 'David'}
long_names = {name for name in names if len(name) > 5}
print(long_names)  # Output: {'Charlie'}




# Set Methods

# Example 1: Using the union() method to compute the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Example 2: Using the intersection() method to compute the intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Example 3: Using the difference() method to compute the difference between two sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Example 4: Using the symmetric_difference() method to compute the symmetric difference between two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Example 5: Using the update() method to update a set with elements from another set
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# Example 6: Using the intersection_update() method to update a set with the intersection of itself and another set
set1.intersection_update(set2)
print(set1)  # Output: {3}

# Example 7: Using the difference_update() method to update a set with the difference between itself and another set
set1.difference_update(set2)
print(set1)  # Output: set()

# Example 8: Using the symmetric_difference_update() method to update a set with the symmetric difference between itself and another set
set1.symmetric_difference_update(set2)
print(set1)  # Output: {4, 5}




# Frozen Sets

# Frozen Sets

# What are frozen sets?
# - Frozen sets are immutable sets in Python.
# - Once created, the elements of a frozen set cannot be modified, added, or removed.

# Characteristics of frozen sets
# - Immutable: Elements of a frozen set cannot be modified after creation.
# - Unordered: Like sets, frozen sets do not maintain any specific order for their elements.
# - Unique Elements: Frozen sets cannot contain duplicate elements.

# Creating and using frozen sets
# - Frozen sets are created using the frozenset() constructor.
# - Frozen sets are useful when you need to create a set of immutable elements.

# Example: Creating a frozen set
frozen_set = frozenset({1, 2, 3, 4})
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})

# Example: Attempting to modify a frozen set (will result in AttributeError)
# frozen_set.add(5)  # Raises AttributeError: 'frozenset' object has no attribute 'add'


# Example 1: Creating a frozen set using the frozenset() constructor
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})

# Example 2: Attempting to add elements to a frozen set (results in an error)
try:
      frozen_set.add(5)
except AttributeError as e:
      print(e)
      # Output: 'frozenset' object has no attribute 'add'

# Example 3: Attempting to remove elements from a frozen set (results in an error)
try:
      frozen_set.remove(3)
except AttributeError as e:
      print(e)
      # Output: 'frozenset' object has no attribute 'remove'

# Example 4: Checking membership in a frozen set
if 2 in frozen_set:
      print("Element 2 is present")
      # Output: Element 2 is present



