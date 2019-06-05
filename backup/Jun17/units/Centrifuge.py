#!/usr/bin.python3.6
class Centrifuge:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=3
		self.defaultBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={
		"gold":3,
		"green":2,
		"blue":2,
		"red":2
		}

	def __str__(self):
		return "Centrifuge"

	def startTurn(self):
		self.owner.destroy(self)
		return True

	def info(self):
		print("Health: "+str(self.health))

def CentrifugeCost():
	buyCostDict={
		"gold":5
	}
	
	return buyCostDict,False,1,[],"Centrifuge"