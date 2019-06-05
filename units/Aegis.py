#!/usr/bin/python3.6
class Aegis:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=5
		self.fragile=True
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Aegis"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile}

def AegisCost():
	buyCostDict={
		"gold":6,
		"green":3
	}
	
	return buyCostDict,False,10,[],"Aegis"