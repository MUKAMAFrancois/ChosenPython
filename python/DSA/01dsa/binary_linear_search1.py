# #1. what is an algorithm?

# An algorithm is a set of step-by-step instructions or rules designed
# to solve a specific problem or perform a particular task. 
# It is a sequence of unambiguous and finite steps that, when followed, 
# produce the desired output from a given input. 


# In the context of Data Structures and Algorithms (DSA), 
# an algorithm is a well-defined procedure that takes some input data and 
# performs a series of operations on that data to produce the desired output. 
# Algorithms are designed to be efficient, meaning they should 
# produce the correct output using minimal resources, such as time and memory.


# Algorithms can be expressed in various ways, 
# including pseudocode, flowcharts, or programming languages like Python. 
# The primary characteristics of a good algorithm are:

# 1. **Finiteness**: An algorithm must terminate after a finite number of steps.
# 2. **Definiteness**: Each step of an algorithm must be precisely defined, with no ambiguity.
# 3. **Input**: An algorithm should have zero or more inputs.
# 4. **Output**: An algorithm should produce at least one output.
# 5. **Effectiveness**: An algorithm should be effective, meaning it should produce the desired output for every input instance.



# 2. What is a data structure?

# A data structure is a way of organizing and storing data in
# a computer's memory so that it can be accessed and manipulated efficiently. 

# It is a particular way of arranging data in a computer's memory or external storage devices for efficient use by a program.
# Data structures are fundamental building blocks in computer programming and are used to implement efficient algorithms.
# They define the relationship between data elements and provide a way to store and retrieve data. 
# Different data structures are suitable for different 
# types of applications and have their own advantages and disadvantages in terms of time and space complexity.


# Data structures can be broadly classified into two categories:
# 1. **Primitive Data Structures**: These are basic data structures provided by the programming language,
# such as integers, floating-point numbers, characters, and pointers.
# 2. **Abstract Data Structures (ADTs)**: These are more complex data structures that are defined by the programmer
# and implemented using primitive data structures. Examples include arrays, linked lists, stacks, queues, trees, and graphs.




# 1.=> Linear Search Algorithm


# The Linear Search algorithm is a simple and fundamental searching algorithm 
# used to find the position or index of a target element within a given sequence,
# such as an array or a list. It is called "linear" because it searches the elements one by one, 
# sequentially, from the beginning to the end of the sequence 
# until the target element is found or the entire sequence is traversed.


# Here's how the Linear Search algorithm works:

# *Start from the first element of the sequence.
# *Compare the current element with the target element.
# *If the current element matches the target element, return its position or index.
# *If the current element does not match the target element, move to the next element in the sequence.
# *Repeat steps 2-4 until either the target element is found or the end of the sequence is reached.
# *If the target element is not found after traversing the entire sequence, return a value indicating that the element is not present (e.g., -1).



def linear_search(listObj,target):

    for i in range(len(listObj)):
        if listObj[i] == target:
            return i
    return None



def verify(index):

    if isinstance(index,int):
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")


numbers=[num for num in range(1,11)]
target=5
index=linear_search(numbers,target)
verify(index) # Target found at index: 4




# 2.=> Binary Search Algorithm

# Binary Search is an efficient algorithm for finding the position or index of a target element in a sorted array or list. It follows a divide-and-conquer approach, repeatedly dividing the search interval in half until the target element is found or determined not to exist in the array.


# Prerequisite: The array or list must be sorted in ascending or descending order.
# Steps:
# a. Initialize two pointers: low (pointing to the first element) and high (pointing to the last element) of the sorted array or list.
# b. Calculate the middle index as mid = (low + high) // 2.
# c. Compare the element at the middle index (arr[mid]) with the target element.
# d. If the element at the middle index is equal to the target element, return the middle index as the position of the target element.
# e. If the element at the middle index is greater than the target element, the target must lie in the left half of the array. Update high = mid - 1 and go to step b.
# f. If the element at the middle index is smaller than the target element, the target must lie in the right half of the array. Update low = mid + 1 and go to step b.
# g. If the loop terminates without finding the target element, return an appropriate value (e.g., -1) indicating that the element is not present in the array.
# Time Complexity:

# The time complexity of Binary Search is O(log n), 
# where n is the size of the input array or list. 
# This logarithmic time complexity makes Binary Search highly efficient for large sorted data sets.


# Space Complexity:

# The space complexity of Binary Search is O(1), 
# as it uses a constant amount of extra space, regardless of the input size.




def binary_search(listObj,target):
    
    first =0
    last =len(listObj)
    
    while first <= last:
        midpoint = (last + first) // 2
        
        if listObj[midpoint] == target:
            return midpoint
        
        else:
            if target < listObj[midpoint]:
                last = midpoint
            elif target > listObj[midpoint]:
                first = midpoint
    


def verify(index):

    if isinstance(index,int):
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")
        
numbers=[num for num in range(0,11)]
target=5
index=binary_search(numbers,target)
verify(index) 

        
        