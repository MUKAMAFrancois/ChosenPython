

# ****************LAMBDA FUNCTIONS*****************


#sol1.
def incrementBy5(increment=5):
    result = lambda number : number +increment
    return result

add5 = incrementBy5()
print(add5(90))


multiplier = lambda x,y : x*y
product = multiplier(10,23)
print(product)




# sol2


def multiplyByAny(multiplyBy):
    return lambda number: number * multiplyBy

double=multiplyByAny(2)
print(double(20))



# sol3



def sortList_ofTuple(arr):
    arr.sort(key=lambda y : y[1])
    return arr


tup=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sortList_ofTuple(tup)) 
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]




# sol4



items=[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
        ]

soted_items = sorted (items, key =lambda y: int(y['model']),reverse=True)
for item in soted_items:
    print(item)


# sol5



# def startsWith_(sentence,ch):
#     return sentence.startswith(ch)

# print(startsWith_("SWE","S"))

def starting_with(ch):
    return lambda sentence: sentence.lower().startswith(ch.lower())

startQ=starting_with("Q")
decision =startQ("Quadrature")
print(decision)



# sol6



def separator(theTime):
    year_time = theTime.split()
    year_mon_date=year_time[0].split('-')

    print(f"Year: {year_mon_date[0]}, Month: {year_mon_date[1]}, Date: {year_mon_date[2]}.")
    print(f"Time is: {year_time[1]}")

year="2020-01-15 09:03:32.744178"
separator(year)



# using Lambda

separator=lambda theTime : print(f"The year: {theTime.split()[0].split('-')[0]} \n The Month: {theTime.split()[0].split('-')[1]} \n The Date: {theTime.split()[0].split('-')[2]} \n The time: {theTime.split()[1]}")
year="2020-01-15 09:03:32.744178"
print(separator(year))

# The year: 2020 
#  The Month: 01
#  The Date: 15
#  The time: 09:03:32.744178





# Sol7



student_info = {
    'Alice': {'age': 25, 'major': 'Computer Science'},
    'Bob': {'age': 23, 'major': 'Engineering'},
    'Charlie': {'age': 22, 'major': 'Mathematics'}
}



sortedbyAge={
    name:info for name,info in sorted(student_info.items(),key=lambda y: y[1]['age'],reverse=True)
}

print(sortedbyAge)





# ************************LISTS************************************

# sol1. 


list1 =[22,33,44]
emp=""
for number in list1:
    emp = emp + str(number)
    
print(emp)





# Sol2


students = [
    {"student1": {"age": 23, "class": "ETE"}},
    {"student2": {"age": 43, "class": "E23"}},
    {"student3": {"age": 30, "class": "EKE"}}
]


def sortedList(listQ):
    sortedL = sorted(listQ, key=lambda x: list(x.values())[0]['age'])
    print(sortedL)

sortedList(students)
# [{'student1': {'age': 23, 'class': 'ETE'}}, {'student3': {'age': 30, 'class': 'EKE'}}, {'student2': {'age': 43, 'class': 'E23'}}]




# sol3


greater=[]
smpList=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
for index in range(len(smpList)):
    if sum(smpList[index]) >sum(greater):
        greater=smpList[index]

print(greater)




# Sol4. 

duplicated= [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
uniques=[]
for singleList in duplicated:
    if singleList not in uniques:
        uniques.append(singleList)

print(uniques)





# sol5

list1= ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

def starting_with(list_obj):
    startW=[]
    letter = input("Enter char: ")
    for element in list_obj:
        if element.startswith(letter):
            startW.append(element)
    print(startW)

starting_with(list1)



# sol6


# isinstance() is a built-in Python function that checks whether 
# an object is an instance of a specified class or of any of its subclasses. It takes two arguments: 
# the object to be checked and the class (or tuple of classes) to check against.
# isinstance(object, classinfo)
x = 5
print(isinstance(x, int))  # True, because x is an instance of the int class
print(isinstance(x, float)) # False, because x is not an instance of the float class


def check_empty_dicts(list_of_dicts):
    for dict_item in list_of_dicts:
        if not isinstance(dict_item, dict) or bool(dict_item):
            return False
    return True

# Test cases
print(check_empty_dicts([{}, {}, {}]))    # True
print(check_empty_dicts([{1, 2}, {}, {}])) # False



# Sol7.

originalList=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

def flattening(listObj):
    flattened=[]
    for sth in listObj:
        if not isinstance(sth,list):
            flattened.append(sth)
        else:
            for element in sth:
                flattened.append(element)
    
    print(flattened)

flattening(originalList)


# Sol8.



def consecutiveDuplicateRemover(listObj):
    conseDupRemoved = [listObj[0]]  # Add the first element to the result list

    for index in range(1, len(listObj)):
        if listObj[index] != listObj[index - 1]:  # Check if the current element is different from the previous one
            conseDupRemoved.append(listObj[index])  # If it's different, append it to conseDupRemoved

    return conseDupRemoved

original = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
result = consecutiveDuplicateRemover(original)
print("After removing consecutive duplicates:")
print(result)


# Sol9.



def subListsMaker(listObj):
    container=[]
    
    for element in listObj:
        if container and element == container[-1][-1]:
            #if container is not empty, and 
            # has the last element of sublist is same as current element
            container[-1].append(element)
        else:
            container.append([element])
    
    return container
    
original =[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

print(subListsMaker(original))
