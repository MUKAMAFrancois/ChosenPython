# Recursion is a programming technique where a function calls itself to solve a problem.

# Base Case: A condition that stops the recursion. 
# Without a base case, the function would recurse indefinitely, leading to a stack overflow error.



def factorial(n):

    if n ==0:
        return 1
    
    else:
        return n * factorial(n-1)
    

print(factorial(5)) # 120




# fibonacci series : 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,...


def fibonacci(n):
    # Base cases: fibonacci of 0 is 0, fibonacci of 1 is 1
    if n <= 1:
        return n
    else:
        # Recursive case: fib(n) = fib(n-1) + fib(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8




#ex3. Binary Search Algorithm
def recursive_binary_search(lst,target,low=0,high=None):
    if high is None:
        high=len(lst)-1
    
    if low <= high:
        mid = (low+high)//2
        
        if lst[mid] == target:
            return mid
            
        else:
            if target>lst[mid]:
                return recursive_binary_search(lst,target,mid+1,high)
            else:
                return recursive_binary_search(lst,target,low,mid-1)
    return "Index not found"
    
    
def verify(index):

    if isinstance(index,int):
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")
        
numbers=[num for num in range(0,11)]
target=5
index=recursive_binary_search(numbers,target)
verify(index) 