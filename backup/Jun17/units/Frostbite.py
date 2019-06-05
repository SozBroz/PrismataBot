#!/usr/bin.python3.6
class Frostbite:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Frostbite"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.destroy(self)
		self.owner.freeze(3)

	def info(self):
		print("Health: "+str(self.health))

def FrostbiteCost():
	buyCostDict={
		"gold":2,
		"red":1
	}
	
	return buyCostDict,True,20,[],"Frostbite"