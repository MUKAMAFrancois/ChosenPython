# 1. Write a Python program to remove duplicates from the dictionary.

# Sample dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 2}
# Expected output: {'a': 1, 'b': 2, 'c': 3}



unique_dict={}
sample={'a': 1, 'b': 2, 'c': 3, 'd': 2}

for key, value in sample.items():
    if value not in unique_dict.values():
        unique_dict[key]=value
        
print(unique_dict)

#2.
# Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


result={}

def combiner(dict1, dict2):
    for key in dict1.keys():
        if key in dict2.keys():
            result[key] = dict1[key] + dict2[key]
        else:
            result[key]=dict1[key]
            
    for key,value in dict2.items():
        if key not in result.keys():
            result[key]=value
            
    return result
print(combiner(d1,d2))

#3. (w3....21)
# Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd