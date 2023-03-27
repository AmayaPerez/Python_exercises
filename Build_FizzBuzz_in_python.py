'''
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"


we are going to use:
    *Function
    *Lopping
    *Conditionals
    *Math operators

We have to be careful with ythe order of conditionals because if you get that mixed up then it can lead to some confusing behavior.
'''

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

fizzbuzz()



