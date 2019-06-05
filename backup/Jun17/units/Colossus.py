#!/usr/bin.python3.6
class Colossus:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=8
		self.fragile=True
		self.attack=3
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":3
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Colossus"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def ColossusCost():
	buyCostDict={
		"gold":15,
		"green":1,
		"blue":2,
		"red":2
	}
	
	return buyCostDict,True,4,[],"Colossus"