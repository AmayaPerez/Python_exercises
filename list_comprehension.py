'''
Coding Exercise
Create a variable called result and use list comprehension to increment each number from the numbers list by 1.

'''
def list_comprehension():
    numbers = [1,2,3,4,5,6]
    # Write your code here
    result = []
    result = [number ++ 1 for number in numbers]
    
    return result