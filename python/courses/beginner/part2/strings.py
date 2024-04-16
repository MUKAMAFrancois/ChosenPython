

# 1. **String Basics**:
#    - String declaration and assignment
#    - String indexing and slicing
#    - String length and character access

my_string = "Python is awesome!"

# Indexing
print(my_string[0])  # Output: P
print(my_string[6])  # Output: i

# Slicing
print(my_string[0:6])  # Output: Python
print(my_string[7:10])  # Output: is
print(my_string[-1])  # Output: !
print(my_string[-5:])  # Output: some!






my_string = "Python is awesome!"

# String length
print(len(my_string))  # Output: 18

# Accessing characters
print(my_string[0])  # Output: P
print(my_string[4])  # Output: o
print(my_string[-1])  # Output: !


# 2. **String Formatting**:
#    - String concatenation
#    - String interpolation (f-strings, `.format()`)
#    - String multiplication




# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe



# String interpolation using f-strings
age = 30
message = f"My name is {first_name} {last_name} and I am {age} years old."
print(message)  # Output: My name is John Doe and I am 30 years old.




# String formatting using .format()
message = "My name is {} {} and I am {} years old.".format(first_name, last_name, age)
print(message)  # Output: My name is John Doe and I am 30 years old.


# String multiplication
greeting = "Hello, "
repeated_greeting = greeting * 3
print(repeated_greeting)  # Output: Hello, Hello, Hello,

# 3. **String Methods**:
#    - `upper()`, `lower()`, `title()`, `swapcase()`
#    - `strip()`, `lstrip()`, `rstrip()`
#    - `replace()`, `split()`, `join()`
#    - `find()`, `index()`, `count()`


# String methods for case conversion
text = "Hello, World!"

# Convert to uppercase
print(text.upper())  # Output: HELLO, WORLD!

# Convert to lowercase
print(text.lower())  # Output: hello, world!

# Convert to title case (first letter of each word is uppercase)
print(text.title())  # Output: Hello, World!

# Swap the case of each character
print(text.swapcase())  # Output: hELLO, wORLD!

# The upper() method converts all characters in the string to uppercase.
# The lower() method converts all characters in the string to lowercase.
# The title() method converts the first character of each word to uppercase, and the rest to lowercase.
# The swapcase() method swaps the case of each character in the string



# String methods for removing whitespace
text = "   Hello, World!   "

# Remove whitespace from both ends
print(text.strip())  # Output: "Hello, World!"

# Remove whitespace from the left side
print(text.lstrip())  # Output: "Hello, World!   "

# Remove whitespace from the right side
print(text.rstrip())  # Output: "   Hello, World!"

# The strip() method removes whitespace (spaces, tabs, newlines) from both the beginning and the end of the string.
# The lstrip() method removes whitespace from the left (beginning) of the string.
# The rstrip() method removes whitespace from the right (end) of the string.



# String methods for manipulation
text = "Apple, Banana, Cherry"

# Replace a substring
print(text.replace("Banana", "Orange"))  # Output: "Apple, Orange, Cherry"

# Split a string into a list
print(text.split(", "))  # Output: ['Apple', 'Banana', 'Cherry']

# Join a list of strings into a single string
fruits = ["Apple", "Banana", "Cherry"]
print(", ".join(fruits))  # Output: "Apple, Banana, Cherry"





# String methods for searching and counting
text = "The quick brown fox jumps over the lazy dog."

# Find the index of a substring
print(text.find("quick"))  # Output: 4
print(text.find("elephant"))  # Output: -1 (not found)

# Find the index of a substring (raises ValueError if not found)
print(text.index("quick"))  # Output: 4
# print(text.index("elephant"))  # ValueError: substring not found

# Count the occurrences of a substring
print(text.count("the"))  # Output: 2 (case-insensitive)
print(text.count("The"))  # Output: 1


# 4. **Escape Sequences**:
#    - Newline, tab, backslash, and other special characters

# Newline
print("Hello,\nWorld!")
# Output:
# Hello,
# World!

# Tab
print("Hello,\tWorld!")
# Output:
# Hello,     World!

# Backslash
print("This is a backslash: \\")
# Output:
# This is a backslash: \

# Single quote
print('This is a single quote: \'')
# Output:
# This is a single quote: '

# Double quote
print("This is a double quote: \"")
# Output:
# This is a double quote: "

# Unicode character
print("Unicode character: \u2713")
# Output:
# Unicode character: ✓

# 5. **Multiline Strings**:
#    - Triple-quoted strings
#    - Escape characters in multiline strings

# Multiline string using triple quotes
multiline_string = """This is the first line.
This is the second line.
This is the third line."""

print(multiline_string)
# Output:
# This is the first line.
# This is the second line.
# This is the third line.



# 6. **String Comparisons**:
#    - Equality and inequality comparisons
#    - Lexicographical ordering

# Strings are compared character by character, from left to right.
# Comparisons are case-sensitive by default.
# The comparison is based on the Unicode code point of each character.

# Equality and inequality comparisons
print("apple" == "apple")  # True
print("apple" != "banana")  # True
print("apple" < "banana")  # True
print("apple" > "Banana")  # True (case-sensitive)
print("apple" <= "apple")  # True
print("apple" >= "banana")  # False


# The sorted() function can be used to sort a list of strings in lexicographical order.
# Capitalization is considered in the sorting order (uppercase comes before lowercase).
# Numbers within the strings are sorted numerically, not lexicographically.


# Lexicographical ordering
print(sorted(["apple", "banana", "cherry", "date"]))
# Output: ['apple', 'banana', 'cherry', 'date']

print(sorted(["apple", "Apple", "APPLE"]))
# Output: ['APPLE', 'Apple', 'apple']

print(sorted(["apple10", "apple2", "apple1"]))
# Output: ['apple1', 'apple10', 'apple2']

# 7. **Unicode and Character Encoding**:
#    - Unicode character sets (ASCII, UTF-8, etc.)
#    - Handling non-ASCII characters


# Using non-ASCII characters
name = "José"
print(name)  # Output: José

# Mixing ASCII and non-ASCII characters
greeting = f"Hello, {name}!"
print(greeting)  # Output: Hello, José!


# Reading from a file with non-ASCII characters
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Writing to a file with non-ASCII characters
with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Hello, José!")

# 8. **String Manipulation Techniques**:
#    - Reversing a string
#    - Checking for palindromes
#    - Removing duplicates from a string
#    - Generating random strings
    

    # Reversing a string
original_string = "Python"
reversed_string = original_string[::-1]
print(reversed_string)  # Output: nohtyP


# Checking for palindromes
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False


# Removing duplicates from a string
original_string = "Hello, World!"
unique_characters = "".join(set(original_string))
print(unique_characters)  # Output: "H, el Wrd!o"


import random
import string

# Generating random strings
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(10)
print(random_string)  # Output: "Ht7Xf2Jk3P"

# 9. **Regular Expressions (Regex)**:
#    - Matching patterns in strings
#    - Searching, substituting, and splitting strings using regex

import re

# Matching patterns in strings
text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w+\b"  # Match whole words

matches = re.findall(pattern, text)
print(matches)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']




# Searching for a pattern
if re.search(r"\d+", text):
    print("Found a number in the text.")

# Substituting a pattern
new_text = re.sub(r"\b\w{4}\b", "****", text)
print(new_text)  # Output: The **** brown **** **** over the **** ****.

# Splitting a string using a pattern
parts = re.split(r"[ .]", text)
print(parts)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '']

# 10. **String Performance and Memory Management**:
#     - Immutability of strings
#     - String interning
#     - Avoiding unnecessary string concatenation

# Immutability of strings
name = "Alice"
name[0] = "B"  # TypeError: 'str' object does not support item assignment


# String interning
a = "hello"
b = "hello"
print(a is b)  # True


# In the example above, both a and b refer to the same string object in memory, as Python automatically interned the string "hello"  