#!/usr/bin/python3.6
class Animus:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=2
		self.fragile=False
		self.attack=0
		self.startTurnDict={
		"red":2
		}

	def __str__(self):
		return "Animus"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def AnimusCost():
	buyCostDict={
		"gold":6
	}
	
	return buyCostDict,False,10,[],"Animus"