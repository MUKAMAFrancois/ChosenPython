
# Sol1.

students={
    "Tom":{"age":26,"program":"CS"},
    "Theressa":{"age":23,"program":"IT"},
    "Patrick":{"age":12,"program":"EEE"},
    "Joseph":{"age":21,"program":"Biology"}
}

sorted_students ={
    student:info for student,info in sorted(students.items(), key=lambda y:y[1]['age'])
}
print(sorted_students)


# Sol2. 


def concantenate(dict1,dict2,dict3):
    dict1.update(dict2)
    dict1.update(dict3)

    return dict1


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(concantenate(dic1,dic2,dic3))



# Sol3. 



def dictinary_sq(n):
    return {n:n**2 for n in range(1,n+1)}


print(dictinary_sq(7))




# Sol4. 


ages={
    23:"Alain",
    21:"Samson",
    19:"Aaron",
    32:"Abraham"
}

sorted_ages ={
    age:student for age,student in sorted(ages.items(),key=lambda y:y[0])
}
print(sorted_ages) #{19: 'Aaron', 21: 'Samson', 23: 'Alain', 32: 'Abraham'}



# Sol6.

ages={
    23:"Alain",
    21:"Samson",
    19:"Aaron",
    32:"Abraham",
    23:"Tresor"
}

print(ages[23])

def removeDuplicates(dictinary):
    unique_dict={}

    for key,value in dictinary.items():
        if key not in unique_dict.keys():
            unique_dict[key] =value
    print(unique_dict)

removeDuplicates(ages)



# Sol7.

nulls={'c1': 'Red', 'c2': 'Green', 'c3': None}

def removeNones(nulls):
    non_nulls={}
    for key,value in nulls.items():
        if value !=None:
            non_nulls[key]=value
    
    print(non_nulls)

removeNones(nulls)


# Sol8.

dict1={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}


def get_max_min(dict1):
    sorted_items= [{name:age} for name,age in sorted(dict1.items(), key= lambda y:y[1])]
    
    first=sorted_items[0]
    last=sorted_items[-1]
    lis1=[]
    for key1 in last.keys():
        lis1.append(key1)
        
    for key in first.keys():
        lis1.append(key)
    

    print(tuple(lis1))

get_max_min(dict1) #('Roxanne', 'Theodore')



# Sol9.

def dict2lists(dict1):
    nestedLists=[
        [key,value] for key,value in dict1.items()
    ]
    return nestedLists


colors={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

print(dict2lists(colors))


# Sol10.

values={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

def first_N_maximums(dict_values):
    sorted_values=[
    {letter:number} for letter,number in sorted(dict_values.items(),key=lambda y:y[1],reverse=True)
]
    N_maximums=int(input("How many first maximums?: "))
    result=[]
    for index in range(N_maximums):
        for key in sorted_values[index].keys():
            result.append(key)

    print(result)

first_N_maximums(values)


# Sol11.

dict1={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

def frequency_counter(dictinary):
    counts={}

    for value in dictinary.values():
        if value in counts.keys():
            counts[value] +=1
        else:
            counts[value] =1
    
    print(counts)

frequency_counter(dict1)


# Sol12.



x={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
y={'x': 300, 'y': 'Red', 'z': 600}
output={'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
def list_of_values(dict1,dict2):
    result={}

    for key,value in dict1.items():
        result[key] = [value]
    
    for key,value in dict2.items():
        if key in result.keys():
            result[key].append(value)
        else:
            result[key] = value
    
    print(result)


list_of_values(x,y)




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


# OR

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


# output

def combiner(d1,d2):
    d={}
    for name in d1.keys():
        if name in d2.keys():
            d[name] = d1[name] + d2[name]
        elif name not in d2.keys():
            d[name] = d1[name]
        else:
            d[name] = d2[name]
    print(d)

combiner(d1=d1,d2=d2)

#3. (w3....21)
# Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd






#### LISTS #################33



