#!/usr/bin.python3.6
class Thunderhead:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=3
		self.frontline=True
		self.cooldown=1
		self.defaultBlocking=True
		self.health=11
		self.fragile=False
		self.attack=4
		self.startTurnDict={
		"attack":4
		}

	def __str__(self):
		return "Thunderhead"

	def startTurn(self):
		return True

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Frontline:"+self.frontline)
		print("Health: "+str(self.health))

def ThunderheadCost():
	buyCostDict={
		"gold":15,
		"green":5,
		"blue":1
	}
	
	return buyCostDict,False,1,[],"Thunderhead"