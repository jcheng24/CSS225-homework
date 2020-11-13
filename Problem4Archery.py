#Name of File: Problem 4
#
#Programmer name: Jada Cheng
#Date Published: 11/10/20
#
#Description of what the program does: 
#
#Description of known issues: Line 35, I do not know how to sum all the numbers 

import random

score = 0
arrow = 10
score_card = []

count = 0
while count < 10:
    count += 1
    arrow -= 1
    score = (random.randint(0,10))
    score_card.append(score)
    
    if score == 0:
        count -= 1
        arrow += 1
        
    elif score == 10:
        score_card.remove(10)
        score_card.append(20)
        
    print(score)
print(score_card)


print("Final Score:",score)
print("Score Card:",sum(score_card))
