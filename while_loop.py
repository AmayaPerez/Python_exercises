
'''
Coding Exercise
In the below starter code, place 4 dog names (elements) of your choice in the dog_house list. Then write a while loop that iterates through the dog_house list and prints each dogs name. An iterator variable named "counter" must be set, and must have an initial value of 0.

Hint: An iterator value (also sometimes called a sentinel value) is a value that exists outside of your loop, and that you update or otherwise keep track of each time you loop, so that your while loop knows when to end.

Example:
iterator_value = 0
while iterator_value < 10:
    print("Keep looping...")
    iterator_value += 1
'''

def loop_using_while():
    dog_house = ["Yako", "Toby", "Luna", "Kira"] # Put dog names here
    counter = 0
    while counter < 4:
        print(dog_house[counter])
        counter += 1
       
    
    
    return [dog_house, counter]
    