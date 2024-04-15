### from: https://www.w3resource.com/python-exercises/lambda/index.php


<!-- LAMBDAS -->
1.  Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

Sample Output:
25
48


2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75



3.  Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]




4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :

[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]



5. Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False

6. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178


7. Sort this by Age:
student_info = {
    'Alice': {'age': 25, 'major': 'Computer Science'},
    'Bob': {'age': 23, 'major': 'Engineering'},
    'Charlie': {'age': 22, 'major': 'Mathematics'}
}





<!-- LISTS -->

1.  Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350

2.  Write a Python program to sort a list of nested dictionaries.

3. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]

4.  Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]] => Qn 69.


5. Write a Python program to find items starting with a specific character from a list.
Expected Output:
Original list:
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]


6. Write a Python program to check whether all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False

7. Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


8. Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

9. . Write a  Python program to pack consecutive duplicates of a given list of elements into sublists.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

10. . Write a  Python program to split a given list into two parts where the length of the first part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1]) => Qn79