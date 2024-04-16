def value_replacement(array,value):
    str_arr =[]
    for element in array:
        str_arr.append(str(element))

    str_text=",".join(str_arr)
    replaced_text=str_text.replace(str(value),"_")
    replaced_arr_str=sorted(replaced_text.split(","))
    
    solution=[]
    for j in replaced_arr_str:
        if j !='_':
            solution.append(int(j))
        else:
            solution.append('_')

    print(solution)


nums = [0,1,2,2,3,0,4,2]
val = 2
value_replacement(array=nums,value=val)

