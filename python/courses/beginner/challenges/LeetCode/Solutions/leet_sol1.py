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
                




# Sol 2.

class Solution:
    def integerToRoman(self, integer):
        roman_numerals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        result = ""
        for numeral, value in roman_numerals.items():
            while integer >= value:
                result += numeral
                integer -= value

        return result

# Example usage
solution = Solution()
print(solution.integerToRoman(456))  # Output: CDLVI