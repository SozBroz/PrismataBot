#!/usr/bin.python3.6
class Cynestra:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=2
		self.fragile=True
		self.attack=3
		self.startTurnDict={
		"attack":3
		}

	def __str__(self):
		return "Cynestra"

	def startTurn(self):
		return True

	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def CynestraCost():
	buyCostDict={
		"gold":12,
		"green":3,
		"red":1
	}
	
	return buyCostDict,False,4,[],"Cynestra"