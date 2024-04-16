# Sol1. 

def solution(n):
    return (n**2 + (n-1)**2)

print(solution(6))




# Sol 2.

def solution(statues):
    missing=[]
    arranged_statues=sorted(statues)
    for number in range(arranged_statues[0],arranged_statues[-1]):
        if number not in arranged_statues:
            missing.append(number)
    
    return missing

print(solution([6, 2, 3, 8]))



# Sol3........... ?????????........



def solution(sequence):
    count = 0  # Counter to keep track of removed elements

    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            count += 1
            if count > 1:
                return False

            # Check if removing the current or previous element would result in a strictly increasing sequence
            if i > 1 and sequence[i] <= sequence[i - 2]:
                sequence[i] = sequence[i - 1]
            else:
                sequence[i - 1] = sequence[i]

    return True



print(solution([1, 3, 2, 1]))  # Output: False
print(solution([1, 3, 2]))  # Output: True


#Sol4.

# 

# Problem Explanation:
# Given an array of integers, we need to check each consecutive triple of elements in the array. A triple (a, b, c) is considered a zigzag if either a < b > c or a > b < c. Our task is to construct a new array where the ith element of the output array is 1 if the corresponding triple in the original array is a zigzag, and 0 otherwise.

# Solution Approach:
# To solve this problem, we can iterate over the array and compare each triple of consecutive elements. If the triple satisfies the zigzag condition, we append 1 to the result array; otherwise, we append 0.

# Here's the beginner-level Python solution:


def solution(numbers):
    result = []

    for i in range(len(numbers) - 2):
        a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
        
        if (a < b > c) or (a > b < c):
            result.append(1)
        else:
            result.append(0)

    return result

numbers = [1, 2, 1, 3, 4]
print(solution(numbers))  # Output: [1, 1, 0]


# Sol5. 


def matrix_elements_sum(matrix):
    total_sum = 0
    haunted_columns = set()  # Keep track of haunted columns

    for row in matrix:
        for col, value in enumerate(row):
            if value == 0:
                haunted_columns.add(col)  # Mark the column as haunted
            elif col not in haunted_columns:
                total_sum += value

    return total_sum

matrix1 = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
print(matrix_elements_sum(matrix1))  # Output: 9

matrix2 = [[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]
print(matrix_elements_sum(matrix2))  # Output: 9



# 

# ```python
# def matrix_elements_sum(matrix):
# ```
# This line defines a function named `matrix_elements_sum` that takes a matrix (a list of lists) as input.

# ```python
#     total_sum = 0
# ```
# This line initializes a variable `total_sum` to 0. This variable will be used to store the sum of the costs of suitable rooms (rooms that are not haunted or below a haunted room).

# ```python
#     haunted_columns = set()
# ```
# This line creates an empty set named `haunted_columns`. This set will be used to keep track of the column indices that have a haunted room (a room with cost 0).

# ```python
#     for row in matrix:
#         for col, value in enumerate(row):
#             if value == 0:
#                 haunted_columns.add(col)
# ```
# These lines iterate over each row in the matrix using a nested loop. For each element in the row, the `enumerate` function is used to get the column index (`col`) and the value (`value`) of the element. If the value is 0 (a haunted room), the column index `col` is added to the `haunted_columns` set.

# ```python
#             elif col not in haunted_columns:
#                 total_sum += value
# ```
# This line checks if the current column index `col` is not in the `haunted_columns` set (meaning it's not a haunted column or below a haunted room). If this condition is true, the value of the current element is added to `total_sum`.

# ```python
#     return total_sum
# ```
# After iterating through all rows and columns, the function returns the `total_sum`, which represents the sum of the costs of suitable rooms.

# The algorithm used here is a straightforward implementation that iterates through the matrix and keeps track of haunted columns. It follows these steps:

# 1. Initialize `total_sum` to 0 and `haunted_columns` to an empty set.
# 2. Iterate through each row in the matrix.
# 3. For each element in the row:
#    a. If the element's value is 0 (a haunted room), add the column index to the `haunted_columns` set.
#    b. If the element's value is not 0 and its column index is not in the `haunted_columns` set (not a haunted column or below a haunted room), add the element's value to `total_sum`.
# 4. After iterating through all rows and columns, return `total_sum`.

# The time complexity of this algorithm is O(m * n), where m is the number of rows and n is the number of columns in the matrix. This is because we need to iterate through all elements in the matrix once.

# The space complexity is O(n), where n is the number of columns, as we need to store the column indices of haunted columns in the `haunted_columns` set. In the worst case, all columns could be haunted, so the set would need to store n elements.




# Sol6.

def solution(inputArray):
    # Step 1: Find the maximum length of strings in the input array
    max_length = max(len(s) for s in inputArray)

    # Step 2: Create a new list to store the longest strings
    longest_strings = []

    # Step 3: Iterate through each string in the input array
    for string in inputArray:
        # Step 4: Check if the length of the current string is equal to the maximum length
        if len(string) == max_length:
            # Step 5: If it is, add the string to the longest_strings list
            longest_strings.append(string)

    # Step 6: Return the list of longest strings
    return longest_strings



# Sol 7.


def solution(s1, s2):
    # Step 1: Create a frequency dictionary for each string
    freq1 = {}
    freq2 = {}

    # Step 2: Count the frequency of each character in s1
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    # Step 3: Count the frequency of each character in s2
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

    # Step 4: Initialize a variable to store the number of common characters
    common_chars = 0

    # Step 5: Iterate through the characters in freq1
    for char in freq1:
        # Step 6: If the character is also present in freq2
        if char in freq2:
            # Step 7: Add the minimum frequency of the character in both strings to common_chars
            common_chars += min(freq1[char], freq2[char])

    # Step 8: Return the number of common characters
    return common_chars



# Sol8.



def solution(n):
    # Convert the ticket number to a string
    n_str = str(n)

    # Calculate the length of the string
    length = len(n_str)

    # Check if the length is even
    if length % 2 != 0:
        return False  # Ticket number must have an even number of digits

    # Calculate the midpoint index
    midpoint = length // 2

    # Calculate the sum of the first half digits
    first_half_sum = sum(int(digit) for digit in n_str[:midpoint])

    # Calculate the sum of the second half digits
    second_half_sum = sum(int(digit) for digit in n_str[midpoint:])

    # Check if the sums are equal
    return first_half_sum == second_half_sum


# Sol9.
def solution(a):
    # Create a list to store the trees
    trees = []
    # Create a list to store the people
    people = []

    # Separate the trees and people
    for height in a:
        if height == -1:
            trees.append(-1)
        else:
            people.append(height)

    # Sort the people in non-descending order
    people.sort()

    # Construct the new list by interleaving trees and people
    result = []
    tree_index = 0
    people_index = 0

    for height in a:
        if height == -1:
            result.append(-1)
            tree_index += 1
        else:
            result.append(people[people_index])
            people_index += 1

    return result



