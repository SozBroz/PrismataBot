#!/usr/bin.python3.6
class Tarsier:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.health=1
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Tarsier"

	def startTurn(self):
		return True

def TarsierCost():
	buyCostDict={
		"gold":4,
		"red":1
	}
	
	return buyCostDict,False,10,[],"Tarsier"