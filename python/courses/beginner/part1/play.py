numbers =[i for i in range(1,12) if i%2==0]
print(numbers) # [2, 4, 6, 8, 10]

index_of_6= numbers.index(6)
print(index_of_6)

numbers[0] =12
print(numbers)