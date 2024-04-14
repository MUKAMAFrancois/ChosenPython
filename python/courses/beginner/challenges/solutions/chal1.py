

# LAMBDA FUNCTIONS


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





# LISTS

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