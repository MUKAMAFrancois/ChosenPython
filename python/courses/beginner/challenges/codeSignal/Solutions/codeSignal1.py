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
# Given an array of integers, we need to check each consecutive triple of elements in the array. 
# A triple (a, b, c) is considered a zigzag if either a < b > c or a > b < c.
#  Our task is to construct a new array where the ith element of the output array is 1 if the corresponding triple in the original array is a zigzag, and 0 otherwise.

# Solution Approach:
# To solve this problem, we can iterate over the array and compare each triple of consecutive elements. 
# If the triple satisfies the zigzag condition, we append 1 to the result array; otherwise, we append 0.



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



# 1. Initialize `total_sum` to 0 and `haunted_columns` to an empty set.
# 2. Iterate through each row in the matrix.
# 3. For each element in the row:
#    a. If the element's value is 0 (a haunted room), add the column index to the `haunted_columns` set.
#    b. If the element's value is not 0 and its column index is not in the `haunted_columns` set (not a haunted column or below a haunted room), add the element's value to `total_sum`.
# 4. After iterating through all rows and columns, return `total_sum`.


inputArray = ["aba", "aa", "ad", "vcd", "aba"]

def sorting(arr):
    longer=[]
    arr.sort(key=lambda y: len(y))
    for item_arr in arr:
        if len(item_arr) == len(arr[-1]):
            longer.append(item_arr)
    print(longer)

sorting(inputArray)




# Sol 7.


str1="backward"
str2="wakeup"
#3: wak
def intersection_chars(str1,str2):
    set1=set()
    set2=set()
    for char in str1:
        set1.add(char)
    for ch in str2:
        set2.add(ch)
    print(len(set1&set2))

intersection_chars(str1,str2)
 



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


def lucky_number(number):
    arr=[]
    arr1=[]
    arr2=[]
    arr1_int=[]
    arr2_int=[]
    for str_num in str(number):
        arr.append(str_num)
    if len(arr) %2 ==0:
        for first_index in range(len(arr)//2):
            arr1.append(arr[first_index])
        for second_index in range(len(arr)//2,len(arr)):
            arr2.append(arr[second_index])
 
        for num in arr1:
            arr1_int.append(int(num))
        for j in arr2:
            arr2_int.append(int(j))
        if sum(arr1_int) == sum(arr2_int):
            print("Lucky")
        else:
            print("Un Lucky")
    else:
        print("No equal parts")
        
    

lucky_number(1230)

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



