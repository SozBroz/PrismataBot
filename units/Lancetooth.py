#!/usr/bin/python3.6
class Lancetooth:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=2
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":2
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Lancetooth"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self): 
		return {
		"health":self.health}

def LancetoothCost():
	buyCostDict={
		"gold":6,
		"blue":1,
		"attack":2
	}
	
	return buyCostDict,True,10,[],"Lancetooth"