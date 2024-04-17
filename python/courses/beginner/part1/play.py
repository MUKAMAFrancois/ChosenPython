def lucky_number(number):
    arr=[]
    arr1=[]
    arr2=[]
    arr1_int=[]
    arr2_int=[]
    for str_num in str(number):
        arr.append(str_num)
    if len(arr) %2 ==0:
        for first_index in range(len(arr)//2):
            arr1.append(arr[first_index])
        for second_index in range(len(arr)//2,len(arr)):
            arr2.append(arr[second_index])
 
        for num in arr1:
            arr1_int.append(int(num))
        for j in arr2:
            arr2_int.append(int(j))
        if sum(arr1_int) == sum(arr2_int):
            print("Lucky")
        else:
            print("Un Lucky")
    else:
        print("No equal parts")
        
    

lucky_number(1230)