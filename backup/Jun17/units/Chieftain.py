#!/usr/bin.python3.6
class Chieftain:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=3
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=7
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
		return "Chieftain"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def ChieftainCost():
	buyCostDict={
		"gold":8,
		"green":2,
		"blue":1
	}
	
	return buyCostDict,True,10,[],"Chieftain"