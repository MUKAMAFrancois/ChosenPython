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