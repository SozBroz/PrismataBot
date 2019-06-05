#!/usr/bin.python3.6
class Immolite:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=1
		self.delay=0
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Immolite"

	def startTurn(self):
		self.delay-=1
		return True

	def canClick(self):
		if self.delay>0:
			return False

		return True

	def onClick(self):
		self.delay=2

	def info(self):
		print("Health: "+str(self.health))
		print("Delay: "+str(self.delay))

def ImmoliteCost():
	buyCostDict={
		"gold":3,
		"red":1
	}
	
	return buyCostDict,True,20,[],"Immolite"