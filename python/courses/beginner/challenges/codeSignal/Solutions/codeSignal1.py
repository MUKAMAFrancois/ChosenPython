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


