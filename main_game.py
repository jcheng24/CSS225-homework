#Remember to put all your files into the same folder on your computer!
#Otherwise, these import statements won't be able to find them properly

#Import all files you'll need to run this properly
import main_character as mc
import the_woman as sc1
import the_shopkeeper as sc2
import section_1
import section_2
import section_3
import section_4
import item


#Create our player character from our main_character class
player = mc.main_character()

#Intro text to the user
#The empty input functions are only here so the player has to type something to move on
#(like pressing a button in a video game to move the dialogue along)

print("Hello there!")
print("Welcome to my game")
input()

#player's name
player.name = input("First, what is your name? ")
print("Cool, hello", player.name)
print("Well, let's get started...")
input()
#And do/say anything else to get your game started

#Then call your first section.
#Be sure to pass in your player character
section_1.start(player)
section_2.start(player)
section_3.start(player)
section_4.start(player)
