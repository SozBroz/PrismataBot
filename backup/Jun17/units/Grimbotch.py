#!/usr/bin.python3.6
class Grimbotch:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=4
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Grimbotch"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))

def GrimbotchCost():
	buyCostDict={
		"gold":4,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Grimbotch"