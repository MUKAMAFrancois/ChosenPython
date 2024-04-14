# Example 5: Unpacking values from nested tuples
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
