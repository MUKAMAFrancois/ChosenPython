# Merge Sort is a popular and efficient sorting algorithm that follows the divide-and-conquer strategy. 
# It works by recursively dividing the input array into two halves,
# sorting each half, and then merging the sorted halves back into a single sorted array.


# Here's how the Merge Sort algorithm works:

# 1. **Base Case**: If the input array contains zero or one element, it is already sorted by definition, so return the array itself.

# 2. **Divide**: If the input array contains more than one element, divide it into two halves by calculating the middle index.

# 3. **Conquer**: Recursively sort the two halves by calling the Merge Sort function on each half.

# 4. **Merge**: Once the two halves are sorted, merge them into a single sorted array by iterating through the two halves and comparing their elements. The smaller element is added to the final sorted array, and the process continues until all elements from both halves are merged.

# Here's an example implementation of the Merge Sort algorithm in Python:


def merge_sort(listObj):
    
    if len(listObj) <=1:
        return listObj
        
    midpoint= len(listObj)//2
    left_half= listObj[:midpoint]
    right_half = listObj[midpoint:]
    
    left=merge_sort(left_half)
    right= merge_sort(right_half)
    
    return merge(left,right)
    

def merge(left,right):
    
    left_index=0
    right_index=0
    merged=[]
    
    while left_index <len(left) and right_index <len(right):
        
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            
            left_index +=1
        
        merged.append(right[right_index])
        right_index +=1
            
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
        
    return merged
    
nums=[34,12,44,2,5]

print(merge_sort(nums))
        
    
    


# In this implementation, the `merge_sort` function recursively divides the input array into two halves until the base case is reached (arrays of length 0 or 1).
# The `merge` function is responsible for merging the sorted halves into a single sorted array.

# The time complexity of Merge Sort is O(n log n) in the average and worst cases, 
# making it an efficient sorting algorithm for large datasets. 
# This time complexity is due to the divide-and-conquer approach and the linear-time merging process.

# Merge Sort has several advantages:

# 1. **Stability**: Merge Sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements in the input array.
# 2. **Efficiency**: The time complexity of O(n log n) is efficient for most practical cases, and the algorithm performs well on large datasets.
# 3. **Space Complexity**: While Merge Sort requires additional space proportional to the input size for the merging process, it can be optimized to operate in-place, reducing the space complexity.
# 4. **Parallelization**: Merge Sort can be easily parallelized, as the division and merging steps can be performed independently on different processors or cores.

# Merge Sort is widely used in various applications, including:

# - External sorting, where data is too large to fit entirely in memory
# - Implementing other algorithms, such as the Timsort algorithm used in Python's `sorted()` and `sort()` functions
# - Parallel computing and distributed systems, where data can be divided and sorted across multiple processors or nodes

# Overall, Merge Sort is a reliable and efficient sorting algorithm that is 
# widely used in computer science and programming due to its time complexity, stability, and ability to be parallelized.







# Let's see merge sort for linked lists.

from ds1 import LinkedList

l= LinkedList()

def merge_sort_linked_list(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list 
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort_linked_list(left_half)
    right = merge_sort_linked_list(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(k log n) time
    """


    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size= linked_list.size()
        mid= size//2

        node_at_mid = linked_list.node_at_index(mid-1)  # size will return the length greater by 1 than the last index
        left_half = linked_list
        right_half = LinkedList() # empty linked list
        right_half.head = node_at_mid.next
        node_at_mid.next = None

        return left_half, right_half
    


def merge(left,right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    """

    merged = LinkedList()

    #set current to the head if the linked list
    current = merged.head
    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
    # If the head node of left is None, we're at the tail
        
        if left_head is None:
            current.next =right_head
            right_head = right_head.next

        # If the head node of right is None, we're at the tail
        elif right_head is None:
            current.next = left_head
            left_head = left_head.next

        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next = left_head
                left_head = left_head.next

            else:
                current.next = right_head
                right_head = right_head.next
        
        current=current.next

    # Discard fake head and set first merged node as head
    head = merged.head.next
    merged.head = head

    return merged


