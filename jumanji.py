#Import and setup the Servo Hat stuff
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#Players

#kit.servo[0].angle=85 magic number to stop the thing from rotating.

player1 = {
	'score':0,
	'skip':False,
	'motor':0,
	'motorstop':88
	}
player2 = {
	'score':0,
	'skip':False,
	'motor':1,
	'motorstop':86
	}
player3 = {
	'score':0,
	'skip':False,
	'motor':2,
	'motorstop':88
	}
player4 = {
	'score':0,
	'skip':False,
	'motor':3,
	'motorstop':87
	}

players = [player1,player2,player3,player4]
dicemax = 3 #maximum dice roll
steps = 7 #number of board positions

#Diceroll Function
def diceroll(dicemax): #roll the dice
	return rand(1,dicemax)

def welcome(): #players the welcome message
	print ('''
	print(chr(27) + "[2J")
		-----------------
		| J U M A N J I |
		-----------------

		Board game something something.
	''')

#STEPS
def step1():
	print(chr(27) + "[2J")
	print ("You stumble upon a hostile wolfpack while beginning your journey. Prove that you are one of them by howling as loud as you can.")

def step2():
	print(chr(27) + "[2J")
	print ("You need to cross a river to continue your journey. Hold your breath for 10 seconds and pretend like you're swimming!")

def step3():
	print(chr(27) + "[2J")
	print ("Monkeys are coming to try to steal your food! Slam the table really hard to scare them away.")

def step5():
	print(chr(27) + "[2J")
	backwards = 6 - rand(1,5) #number of steps you need to take backwards
	print ("You were chased by a buffalo. Move back", backwards, "steps.")
	return backwards

def step6(): 
	print(chr(27) + "[2J")
	print ("You wandered into the wrong part of the forest and were hunted down by an indigenous tribe, who scalped your head and left your bare-skulled body for the nearby anacondas. You die slowly. The other player wins.")

def start_game(dicemax,steps,players):
	turn = 0
	while True:
		if players[turn]['skip'] == False:
			print ("")
			print ("Player", turn+1)
			raw_input("Press ENTER to roll the dice.")
			roll = diceroll(dicemax)
			print ("Player", turn+1, "rolls a", roll)
			
			players[turn]['score'] += roll
			
			print ("Player score", players[turn]['score'])

			#Trigger actions on the step they're on
			if players[turn]['score'] == 6: #dead
				step6()
				break
			if players[turn]['score'] == 5: #move backwards 
				players[turn]['score'] = players[turn]['score'] - step5()
			
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

		if turn == 0:
			turn = 1
		elif turn == 1:
			turn = 0


def game_start(): #start the game
	welcome()
	sleep(1)
	start_game(dicemax,steps,players)

game_start()