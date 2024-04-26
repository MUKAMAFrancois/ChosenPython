# 1. Arrays in python


# append() - Adds an element to the end of the list,
# it's runtime complexity is O(1). means an ammortized constant time complexity.


# insert() - Inserts an element at the specified position in the list.
# The runtime complexity of insert() is O(n) in the worst case, where n is the length of the list.
# This is because inserting an element at a specific position may require shifting all the elements to the right of that position by one index.



# pop() - Removes and returns the element at the specified index (default is the last element).
# Time Complexity: O(1) (constant time)
#  Removing an element from the end of the list is a constant-time operation because the last element 
# can be directly accessed and removed without the need to shift or rearrange other elements.


# Removing an element from the beginning or middle of the list (pop(index)):
# Time Complexity: O(n) (linear time)
# Removing an element from the beginning or middle of 
# the list is a linear-time operation because all the elements after
# the removed element need to be shifted to fill the gap created by the removal.
# This shifting operation requires iterating over the remaining elements, 
# resulting in a time complexity proportional to the size of the list.





# In Python, the `extend()` method is used to add multiple elements from an iterable (such as a list, tuple, or string) 
# to the end of an existing list. The runtime complexity of the `extend()` method depends on the size of the iterable being added to the list.

# **Time Complexity:**
# - Best Case: O(k), where k is the length of the iterable being added
# - Worst Case: O(k + n), where k is the length of the iterable being added, and n is the length of the existing list

# **Explanation:**
# The `extend()` method iterates over the elements in the iterable being added and 
# appends each element to the end of the existing list. This operation involves
#  allocating new memory for the additional elements and potentially resizing the underlying array that stores the list elements.

# In the best case scenario, where the existing list has enough pre-allocated memory to accommodate the new elements, 
# the time complexity is O(k), where k is the length of the iterable being added. This is because the method needs
#  to iterate over the iterable once to copy its elements into the existing list.

# In the worst case scenario, where the existing list does not have enough pre-allocated memory to accommodate the new elements, the list needs to be resized and reallocated in memory. 
# This operation typically involves creating a new, larger array and copying the existing elements from the old array to the new array. 
# The time complexity in this case becomes O(k + n), where k is the length of the iterable being added, and n is the length of the existing list.
#  The additional n component comes from the need to copy the existing elements to the new array.

# Here's an example to illustrate the usage of `extend()`:


fruits = ['apple', 'banana']
more_fruits = ['cherry', 'orange', 'grape']

# Extending the list with more_fruits
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape']


# In the above example, the `extend()` method iterates over the `more_fruits` list and appends each element to the end of the `fruits` list.

# It's important to note that if you only need to concatenate two lists,
# using the `+` operator or the `+=` augmented assignment operator might be more efficient, as these operations leverage efficient list concatenation algorithms in Python's implementation.
# However, if you need to add elements from multiple iterables to a list, using `extend()` can be more convenient
#  and potentially more efficient than concatenating lists repeatedly.






# 2. Linked Lists in Python


# A linked list is a linear data structure composed of nodes, where each node contains a data element and a reference (or pointer) to the next node in the sequence.
#  Unlike arrays, linked lists do not store elements in contiguous memory locations, but rather, they are dynamically allocated and linked together using pointers.
# Here are the key aspects of linked lists:

# Node Structure: Each node in a linked list typically consists of two parts: 
# a data element (which can be of any data type) and a reference (or pointer) that points to the next node in the sequence.

# Head and Tail: The first node of a linked list is called the "head," and the last node is called the "tail."
#  The tail node's reference (or pointer) typically points to null or None, indicating the end of the list.
# Types of Linked Lists:

# Singly Linked List: Each node contains only a reference to the next node in the sequence.
# Doubly Linked List: Each node contains two references: one to the next node and one to the previous node, allowing traversal in both directions.
# Circular Linked List: The last node's reference points back to the head node, forming a circular structure.



class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count
    



#2.1. Operations  on Linked Lists


