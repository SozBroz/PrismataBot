#!/usr/bin.python3.6
class Shadowfang:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=1
		self.attack=2
		self.startTurnDict={
		"attack":2
		}

	def __str__(self):
		return "Shadowfang"

	def startTurn(self):
		return True

def ShadowfangCost():
	buyCostDict={
		"gold":8,
		"red":3
	}
	
	return buyCostDict,False,10,[],"Shadowfang"