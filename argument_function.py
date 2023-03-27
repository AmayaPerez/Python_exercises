
'''
Coding Exercise
Create a function called counter that accepts an argument called initial_count and returns that argument incremented by 1. initial_count must have a default value of 0.
'''

def counter(initial_count = 0):
    count = initial_count ++1
    return count

print(counter())
print(counter(1))


