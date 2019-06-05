#!/usr/bin.python3.6
class FrostBrooder:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=6
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=2
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Frost Brooder"

	def startTurn(self):
		for i in range(0,1):
			owner.player.addUnit("Frostbite,1,3")

		return True

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))

def FrostBrooderCost():
	buyCostDict={
		"gold":5,
		"red":2
	}
	
	return buyCostDict,False,4,[],"Frost Brooder"