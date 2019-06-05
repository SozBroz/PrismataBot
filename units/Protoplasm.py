#!/usr/bin/python3.6
class Protoplasm:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=True
		self.attack=4
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":4
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Protoplasm"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.destroy(self)

	def info(self): 
		return {
		"health":self.health,
		"fragile":self.fragile}

def ProtoplasmCost():
	buyCostDict={
		"gold":7,
		"green":2,
		"red":2
	}
	
	return buyCostDict,True,10,[],"Protoplasm"