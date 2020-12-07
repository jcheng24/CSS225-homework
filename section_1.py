#import anything you need here
import main_character
import random


def start(player):
    #in the forest, came across a split road
    print("Name:",player.name)
    print("Health:",player.hp)
    print("Money:",player.money)
    print("Inventory:",player.inventory)
    input()
    print("You slowly open your eyes...")
    input()
    print("You stare up at the sky to see that it is around early afternoon")
    input()
    print(player.name,": I think it's time to get going.")
    input()
    print("As you are walking down the road, you came across a split end")
    input()
    which_way = input("Which way would you like to go?\n\"L\" - Go left, faller into the forest\n\"R\" - Go right, into town\n\"B\" - Go back to where you were resting")
    input()
    
    #turning back
    if which_way == 'B':
        print(player.name,": I think let's turn back.")
        input()
        print("You turn back")
        input()
        print(player.name,": Wait, you know what...")
        input()
        print(player.name,": Nevermind, let's turn back again.")
        input()
        print(player.name,": I think we should head into to town instead")
        input()
        print("Walking down the right road towards town")
        input()
        print("You have reach the entrance of town")
        input()
    
    #left into the forest
    elif which_way == 'L':
        print(player.name,": I think let's go left.")
        input()
        print("As you are walking faller into the forest...")
        input()
        print("...then...")
        input()
        print("...you suddenly fell off a cliff!")
        input()

        #I tried doing a loop here, but it didn't work. So, here what I have.
        for falling in range(3):
            player.hp -= random.randint(10,15)
            print("*falling*")
            print("Health:",player.hp)
            input()
            player.hp -= random.randint(10,15)
            print("*falling*")
            print("Health:",player.hp)
            input()
            player.hp -= random.randint(10,15)
            print("*falling*")
            print("Health:",player.hp)
            input()
            break
        
        print("That was quite a fall, so it cost a bit of your health")
        input()
        print("Health:",player.hp)
        input()
        print("As you got up, you noticed something in front of you")
        input()
        print("A chest!")
        input()
        print("Walking up to it, you had decided to see what's inside")
        input()
        print("When opening it, there was a bright light shining out of the chest")
        input()
        print("Inside the chest was an orb")
        input()
        print("You weren't sure what it can do so you decided to keep it with you")
        #adding to list
        player.inventory.append("orb")
        input()
        print("You have received a ['orb']")
        print("Inventory:",player.inventory)
        input()
        print("You turn back and climb back to the road that you were on before the fall")
        input()
        print("You walk back to the split end")
        input()
        print("Then you decide to go to town instead, thinking maybe you can sell the orb there")
        input()
        print("You have reach the entrance of town")
        input()
    
    #right into town
    else:
        print(player.name,": I think let's go right.")
        input()
        print("Walking down the right road towards town")
        input()
        print("While walking, you didn't see there was a banana peel on the floor")
        input()
        print("You end up slipping, falling on your back")
        #lose hp
        player.hp -= random.randint(5,8)
        input()
        print("Lost a bit of health there...")
        print("Health:",player.hp)
        input()
        print("You got up and walked it off")
        input()
        print("Finally, you have reach the entrance of town without anymore slipping on banana peels")
        input()

    
