

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



# 4. **Escape Sequences**:
#    - Newline, tab, backslash, and other special characters

# 5. **Multiline Strings**:
#    - Triple-quoted strings
#    - Escape characters in multiline strings

# 6. **String Comparisons**:
#    - Equality and inequality comparisons
#    - Lexicographical ordering

# 7. **Unicode and Character Encoding**:
#    - Unicode character sets (ASCII, UTF-8, etc.)
#    - Handling non-ASCII characters

# 8. **String Manipulation Techniques**:
#    - Reversing a string
#    - Checking for palindromes
#    - Removing duplicates from a string
#    - Generating random strings

# 9. **Regular Expressions (Regex)**:
#    - Matching patterns in strings
#    - Searching, substituting, and splitting strings using regex

# 10. **String Performance and Memory Management**:
#     - Immutability of strings
#     - String interning
#     - Avoiding unnecessary string concatenation

# 11. **Advanced String Operations**:
#     - String templating (Jinja, Mako, etc.)
#     - String encryption and decryption
#     - Parsing and manipulating CSV, JSON, and other text-based data formats

# 12. **String Applications**:
#     - Text processing and data extraction
#     - Natural Language Processing (NLP)
#     - Handling user input and validation

# By covering these topics, you will develop a comprehensive understanding of strings in Python and be able to effectively work with and manipulate text data in your programs.