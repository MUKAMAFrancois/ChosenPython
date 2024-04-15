# 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]


def number_adding_to_target(listObj,target):
    Output=[]
    for index in range(len(listObj)):
        for j in range(1,len(listObj)):
            if listObj[index] + listObj[j] == target:
                Output.append([index,j])
                
    print(Output)
    
    
nums = [9,23,7,21,90,80,22]
target = 30

number_adding_to_target(nums,target)
                
