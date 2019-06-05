#!/usr/bin.python3.6
class Blastforge:
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
		"blue":1
		}

	def __str__(self):
		return "Blastforge"

	def startTurn(self):
		return True

def BlastforgeCost():
	buyCostDict={
		"gold":5
	}
	
	return buyCostDict,False,10,[],"Blastforge"