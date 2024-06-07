#selection sort

# selection sort is not efficient for large lists.
# Time Complexity: O(n^2)


""""
This complexity arises because, in each iteration of selection sort, 
the algorithm selects the smallest (or largest, depending on the sorting order) element from the 
unsorted portion of the array and places it in its correct position. 
To find the smallest element, the algorithm needs to compare it with all other elements in the unsorted portion,
 which requires  ( n - 1  ) comparisons on average. 
 Since there are  ( n  ) elements in total and the algorithm performs this operation for each element, 
 the overall number of comparisons is approximately  (\frac{n(n-1)}{2}  ), resulting in a time complexity of  ( O(n^2)  ).
"""

def selection_sort(values):
  # We'll create an empty list that will hold all our sorted values.
  sorted_list = []
  # We'll loop once for each value in the list.
  for i in range(0, len(values)):
    # We call a function named index_of_min, which we're going to
    # write in just a minute, that find the minimum value in the
    # unsorted list and return its index.
    index_to_move = index_of_min(values)
    # Then we call the "pop" method on the list, and pass it the
    # index of the minimum value. pop will remove that item from the
    # list and return it. We then add that value at the end of the
    # sorted list.
    sorted_list.append(values.pop(index_to_move))
  # Going up a level of indentation signals to Python that we're
  # ending the loop. After the loop finishes, we return the sorted
  # list.
  return sorted_list

# Now we need to write the function that picks out the minimum value.
# We pass in the list we're going to search.
def index_of_min(values):
  # We mark the first value in the list as the minimum. It may or may
  # not be the actual minimum, but it's the smallest we've seen on
  # this pass through the list. (It's also the only value we've seen
  # on this pass through the list so far.)
  min_index = 0
  # Now we loop through the remaining values in the list after the
  # first.
  for i in range(1, len(values)):
    # We test whether the value we're currently looking at is less
    # than the previously recorded minimum.
    if values[i] < values[min_index]:
      # If it is, then we set the current index as the new index of
      # the minimum value.
      min_index = i
  # After we've looped through all the values, we return the index of
  # the smallest value we found.
  return min_index

# Lastly, we need to actually run our selection sort method, and
# print the sorted list it returns.

numbers=[22,34,1,-3,99,7,2,5]
print(selection_sort(numbers))