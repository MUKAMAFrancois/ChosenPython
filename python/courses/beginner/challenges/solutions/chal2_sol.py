
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






#### LISTS #################


# Sol1.  ====????


matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

summed={}
for row in matrix:
    for col,value in enumerate(row):
        if col in summed.keys():
            summed[col]+=value
        else:
            summed[col]=value

column_sums=[]
for value in summed.values():
    column_sums.append(value)


print(summed)
print(column_sums)


# Sol2.


matrix =[
    [20,40,60],
    [10,-10,-20],
    [70,90,100]
]

def sum_of_diagonal(matrix):
    result=0

    for index in range(len(matrix)):
        result += matrix[index][index]

    print(result)

sum_of_diagonal(matrix)


# Sol3.


x=[[1, 3], [5, 7], [9, 11]]
y= [[2, 4], [6, 8], [10, 12, 14]]


def zipping(list1,list2):
    
    for index in range(len(list1)):
        for item in list2[index]:
            list1[index].append(item)
      

    print(list1)


zipping(x,y)


# Sol4.

listObj = [[9, 11], [0], [1, 3], [5, 7], [13, 15, 17]]

listObj.sort(key=lambda x: len(x))
print(listObj)

maximum =(len(listObj[-1]),listObj[-1])
minimum = (len(listObj[0]), listObj[0])
print(maximum,minimum)

# Sol5.


lis1=[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
lis2=[[[3, 4], [5, 6]]]
#expected: True because lis2 is subset of lis1

def isSubset(list1,list2):
    list2_is_subset=0
    count_sub1=0

    for sub_list in list2:
        if sub_list in list1:
            list2_is_subset+=1

    
    for sub_list in list1:
        if sub_list in list2:
            count_sub1 +=1

    if list2_is_subset == len(list2) or count_sub1 == len(list1):
        return True
    else:
        return False
    
print(isSubset(lis1,lis2))


# Sol6.


arr1=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]

def count_occurence_of_element(list1):
    number=int(input("Occurences of?: "))
    occurences=0

    for sublist in list1:
        if number in sublist:
            occurences+=1
    
    print(f"{number} occurs {occurences} times.")


count_occurence_of_element(arr1)


# Sol7.



#Sol8.


#Sol9.


heterogenous =['Python', 3, 2, 4, 5, 'version']

def max_of_mixture(array):
    nums=[]
    for element in array:
        if isinstance(element,int):
            nums.append(element)
    maximum=max(nums)
    minmum=min(nums)
    
    print((maximum,minmum))

max_of_mixture(heterogenous)



