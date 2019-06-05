#!/usr/bin/python3.6
class Bloodrager:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=2
		self.fragile=False
		self.attack=2
		self.startTurnDict={
		"attack":2
		}

	def __str__(self):
		return "Bloodrager"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def BloodragerCost():
	buyCostDict={
		"gold":7,
		"red":1,
		"attack":3
	}
	
	return buyCostDict,False,10,[],"Bloodrager"