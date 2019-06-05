#!/usr/bin.python3.6
class MaharRectifier:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=5
		self.fragile=True
		self.attack=2
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":2
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Mahar Rectifier"

	def startTurn(self):
		self.initHealth=5
		self.health=min(self.health+2,self.initHealth)
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def MaharRectifierCost():
	buyCostDict={
		"gold":11,
		"green":2
	}
	
	return buyCostDict,True,10,[],"Mahar Rectifier"