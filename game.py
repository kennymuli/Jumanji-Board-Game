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

import adafruit_pca9685 as adafruit
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit.PCA9685(i2c)

#Import and setup GPIO
#import RPi.GPIO as GPIO
#button_gpio = 2
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(button_gpio,gpio.IN, pull_up_down=gpio.PUD_DOWN) 
#button = gpio.input(button_gpio)

#########
#PLAYERS#
#########
player1 = {
	'score':0,
	'skip':False,
	'motor':0,
	'motorstop':88,
	'motorspeed' : 90,
	'backwardspeed' : 86,
	'enginetime': 2
	}

players = [player1]
dicemax = 3 #maximum dice roll
steps = 7 #number of board positions

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

def step2():
	print(chr(27) + "[2J")
	print ("You need to cross a river to continue your journey. Hold your breath for 10 seconds and pretend like you're swimming!")
	input()
	print(chr(27) + "[2J")

def step3():
	print(chr(27) + "[2J")
	print ("Monkeys are coming to try to steal your food! Slam the table really hard to scare them away.")
	input()
	print(chr(27) + "[2J")

def step5():
	print(chr(27) + "[2J")
	backwards = 6 - rand(1,5) #number of steps you need to take backwards
	print ("You were chased by a buffalo. Move back", backwards, "steps.")
	return backwards
	input()
	print(chr(27) + "[2J")

def step6(): 
	print(chr(27) + "[2J")
	print ("You wandered into the wrong part of the forest and were hunted down by an indigenous tribe, who scalped your head and left your bare-skulled body for the nearby anacondas. You die slowly. The other player wins.")
	input()
	print(chr(27) + "[2J")

def start_game(dicemax,steps,players):
	turn = 0
	while True:
		if players[turn]['skip'] == False:
			print ("")
			print ("Player", turn+1)
			input("Press ENTER to roll the dice.")
			roll = diceroll(dicemax)
			print ("Player", turn+1, "rolls a", roll)
			
			players[turn]['score'] += roll

			#############
			#SERVO MOTOR#
			#############
			kit.servo[players[turn]['motor']].angle = players[turn]['motorspeed'] #start the engine to move the piece
			sleep(players[turn]['enginetime']*roll)
			kit.servo[players[turn]['motor']].angle = players[turn]['motorspeed'] #stop moving



			##########
			#TRIGGERS#
			##########
			if players[turn]['score'] == 6: #dead
				step6()
				break
			if players[turn]['score'] == 5: #move backwards 
				backwardsteps = step5()
				players[turn]['score'] = players[turn]['score'] - backwardsteps
				kit.servo[players[turn]['motor']].angle = players[turn]['backwardspeed'] #start the engine to move the piece
				sleep(players[turn]['enginetime']*backwardsteps)
				kit.servo[players[turn]['motor']].angle = players[turn]['motorspeed'] #stop moving
			
			if players[turn]['score'] == 4: #skip a turn
				players[turn]['skip'] = True
				print ("Sorry, you're stuck in quicksand!")

			if players[turn]['score'] == 1:
				step1()

			if players[turn]['score'] == 2:
				step2()

			if players[turn]['score'] == 3:
				step3()

			if players[turn]['score'] >= steps: #winner
				print ("Player", turn+1, "wins!")
				break

		else:
			players[turn]['skip'] = False


def game_start(): #start the game
	welcome()
	sleep(1)
	start_game(dicemax,steps,players)

game_start()