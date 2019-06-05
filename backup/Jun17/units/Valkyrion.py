#!/usr/bin.python3.6
class Valkyrion:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=4
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":4
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Valkyrion"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		for i in range(0,2):
			owner.opponent.addUnit("Barrier,1,-1")


	def info(self):
		print("Health: "+str(self.health))

def ValkyrionCost():
	buyCostDict={
		"gold":12,
		"green":2,
		"blue":1,
		"red":1
	}
	
	return buyCostDict,True,4,[],"Valkyrion"