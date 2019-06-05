#!/usr/bin/python3.6
class Amporilla:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=3
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Amporilla"

	def startTurn(self):
		self.owner.resDict["attack"]+=self.owner.numberOfUnit("Tarsier")
		return True

	def info(self): 
		return {
		"health":self.health}

def AmporillaCost():
	buyCostDict={
		"gold":13,
		"red":3
	}
	
	return buyCostDict,False,4,[],"Amporilla"