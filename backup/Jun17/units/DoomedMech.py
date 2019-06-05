#!/usr/bin.python3.6
class DoomedMech:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=5
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=5
		self.fragile=False
		self.attack=2
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":2
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Doomed Mech"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))

def DoomedMechCost():
	buyCostDict={
		"gold":9,
		"blue":2
	}
	
	return buyCostDict,True,10,[],"Doomed Mech"