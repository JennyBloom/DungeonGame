"""
Author: Jenny Bloom
Date: 9/5/2015
Class: CSCI 1310
Assignment: HW2 A Dungeon Game!

This is a text game in Python, with intention of understanding while loops, if/elif/else statements, all the while looking for a princess and avoiding burning to death. 
Basic needs: Quitting, Room, Direction
"""

greeting = "Welcome to Jenny's Dungeon!"
quit_game = "not" #Can be anything!
user_direction = ""
room = "kitchen"


while quit_game != "q":
	if room == "kitchen":
		user_direction = input('You are in the kitchen. There are doors to the west (w), south (s), and east (e).').lower()
		if user_direction == "w":
			room = "hallway"
		elif user_direction == "s":
			room = "furnace" #or quit, and then prompt the goodbye
		elif user_direction == "e":
			room = "living room"
		elif user_direction == "q":
			quit_game = "q"
	elif room == "hallway":
		user_direction = input("You are in the hallway. There are doors to the south (s) and east (e).")
		if user_direction == "s":
			room = "library"
		elif user_direction == "e":
			room = "kitchen"
		elif user_direction == "q":
			quit_game = "q"
	elif room == "living room":
		user_direction = input("You are in the living room. There is a door to the west (w).")
		if user_direction == "w":
			room = "kitchen"
		elif user_direction == "q":
			quit_game = "q"
	elif room == "library":
		user_direction = input("You are in the Library. You found the Princess! You are a Heroine! Goodbye!")
		quit_game = "q"
	elif room == "furnace":
		user_direction = input("You entered the furnace and fry yourself to death! Goodbye!")
		quit_game = "q"
		
			
