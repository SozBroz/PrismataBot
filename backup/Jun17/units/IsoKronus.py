#!/usr/bin.python3.6
class IsoKronus:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.health=5
		self.fragile=True
		self.delay=0
		self.attack=2
		self.startTurnDict={
		"attack":2
		}

	def __str__(self):
		return "Iso Kronus"

	def startTurn(self):
		self.delay-=1
		if self.delay>0:
			return False

		self.delay=2
		return True

	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)
		print("Delay: "+str(self.delay))

def IsoKronusCost():
	buyCostDict={
		"gold":5,
		"green":1
	}
	
	return buyCostDict,False,10,[],"Iso Kronus"