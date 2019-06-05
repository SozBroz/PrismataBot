#!/usr/bin.python3.6
class ArkaSodara:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=7
		self.fragile=False
		self.attack=4
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":4
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Arka Sodara"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

def ArkaSodaraCost():
	buyCostDict={
		"gold":7,
		"blue":2,
		"red":1,
		"attack":7
	}
	
	return buyCostDict,True,1,[],"Arka Sodara"