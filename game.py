#!/usr/bin/env python3

#[x] Setup players
#[x] Servo motor movement
#[x] Players can move backwards
#[x] Setup scenarios and triggers
#[x] Setup dice rolling
#[x] Connect to Servo Hat
#[x] Figure out pins on the Servo Hat for getting input signal
#[ ] LED light-up
#[ ] Receive button signal input
#[ ] Trigger confetti
#[ ] Play animal noises
#[ ] Run on startup
#[ ] Calibrate the servo motors for each player: motorstop, motorspeed, backwardspeed, enginetime

from random import randint as rand
from time import sleep
import board
import busio

#Import and setup the Servo Hat stuff
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#########
#PLAYERS#
#########
player1 = {
	'score':0,
	'skip':False,
	'enginetime': 6
	}

players = [player1]
dicemax = 2 #maximum dice roll
steps = 3 #number of board positions

#Diceroll Function
def diceroll(dicemax): #roll the dice
	return rand(1,dicemax)

def welcome(): #players the welcome message
	
	sleep(0.5)
	print(chr(27) + "[2J")
	print('''
		  ╚⊙ ⊙╝
		  ╚═███═╝
		   ╚═███═╝
		    ╚═███═╝
		    ╚═███═╝     
		   ╚═███═╝      
		    ╚═███═╝     
		     ╚═███═╝     
		     ╚═███═╝    
		    ╚═███═╝
		     ╚═███═╝
		     ╚═███═╝
		    ╚═███═╝
		     ╚═█═╝
	''')
	sleep(0.5)
	print(chr(27) + "[2J")
	print('''
		  ╚⊙ ⊙╝
		 ╚═███═╝
		  ╚═███═╝
		  ╚═███═╝
		   ╚═███═╝     
		   ╚═███═╝      
		    ╚═███═╝     
		     ╚═███═╝     
		     ╚═███═╝    
		    ╚═███═╝
		     ╚═███═╝
		     ╚═███═╝
		    ╚═███═╝
		     ╚═█═╝
	''')
	sleep(0.5)
	print(chr(27) + "[2J")
	print('''
		  ╚⊙ ⊙╝
		 ╚═███═╝
		  ╚═███═╝
		  ╚═███═╝
		   ╚═███═╝     
		   ╚═███═╝      
		  ╚═███═╝     
		   ╚═███═╝     
		    ╚═███═╝    
		   ╚═███═╝
		   ╚═███═╝
		  ╚═███═╝
		   ╚═███═╝
		    ╚═█═╝
	''')
	sleep(0.5)
	print(chr(27) + "[2J")
	print('''
		  ╚⊙ ⊙╝
		 ╚═███═╝
		 ╚═███═╝
		╚═███═╝
		 ╚═███═╝     
		╚═███═╝      
		╚═███═╝     
		╚═███═╝     
		 ╚═███═╝    
		  ╚═███═╝
		   ╚═███═╝
		  ╚═███═╝
		 ╚═███═╝
		 ╚═█═╝
	''')
	sleep(0.5)
	print(chr(27) + "[2J")
	print('''
		  ╚⊙ ⊙╝
		 ╚═███═╝
		 ╚═███═╝
		 ╚═███═╝
		 ╚═███═╝     
		  ╚═███═╝      
		  ╚═███═╝     
		 ╚═███═╝     
		 ╚═███═╝    
		 ╚═███═╝
		  ╚═███═╝
		 ╚═███═╝
		 ╚═███═╝
		  ╚═█═╝
	''')
	sleep(0.5)
	print(chr(27) + "[2J")
	print('''
		  ╚⊙ ⊙╝
		 ╚═███═╝
		 ╚═███═╝
		 ╚═███═╝	|---------------|
		 ╚═███═╝	| J U M A N J I |
		 ╚═███═╝ 	|---------------|
		 ╚═███═╝	A game for those who seek to find 
		 ╚═███═╝	a way to leave their world behind.
		 ╚═███═╝    
		 ╚═███═╝
		 ╚═███═╝
		 ╚═███═╝
		 ╚═███═╝
		  ╚═█═╝
	''')

#STEPS
def step1():
	print(chr(27) + "[2J")
	print ("You stumble upon a hostile wolfpack while beginning your journey. Prove that you are one of them by howling as loud as you can.")
	input()
	print(chr(27) + "[2J")

def backwards():
	print(chr(27) + "[2J")
	backwards = 6 - rand(1,5) #number of steps you need to take backwards
	print ("You were chased by a buffalo. Move back", backwards, "steps.")
	return backwards
	input()
	print(chr(27) + "[2J")

def start_game(dicemax,steps,players,player1,kit):
	turn = 0
	while True:
		print ("")
		input("Press ENTER to roll the dice.")
		roll = diceroll(dicemax)
		print ("You've rolled a", roll)
		print(player1)
		player1['score'] += roll

		#############
		#SERVO MOTOR#
		#############
		kit.servo[0].angle = 88
		sleep(player1['enginetime']*roll)
		kit.servo[0].angle = 86 #stop moving



		##########
		#TRIGGERS#
		##########		
		if players[turn]['score'] == 1:
			step1()

		if players[turn]['score'] == 2:
			backwardsteps = backwards()
			players[turn]['score'] = players[turn]['score'] - backwardsteps
			kit.servo[0].angle = 84 #start the engine to move the piece
			sleep(player1['enginetime']*backwardsteps)
			kit.servo[0].angle = 86 #stop moving

		if players[turn]['score'] >= steps: #winner
			print ("Player", turn+1, "wins!")
			break


def game_start(): #start the game
	welcome()
	sleep(1)
	start_game(dicemax,steps,players,player1,kit)

game_start()