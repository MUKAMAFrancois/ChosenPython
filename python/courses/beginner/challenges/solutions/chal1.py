
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