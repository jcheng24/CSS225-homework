#Name of File: my_module
#
#Programmer Name: Jada Cheng
#Date Published: 11/03/20
#
#Description of what the program does: math
#
#Description of known issues: none?

import random
import math


#problem 1
#for loop to print 10 integers between 25 - 35
for num in range(10):
    print(random.randint(25,35))


#problem 2
#take a list as a parameter and returns a random element from the list
my_list = ("card","mask","shirt","laptop","games")
print(random.choice(my_list))


#problem 3
#return a random odd integer between 0 - 100
odd_rand = random.randrange(1,99,2)
print(odd_rand)


#problem 4
#calculates the Pythagorean theorem using functions
num_1 = int(input("What is a: "))
num_2 = int(input("What is b: "))
num_3 = int(input("What is c: "))

step_1 = (math.pow(num_1,2))
step_2 = (math.pow(num_2,2))
step_3 = (step_1 + step_2)
step_4 = (math.sqrt(step_3))
step_5 = (num_3 - step_4)
print(step_5)
