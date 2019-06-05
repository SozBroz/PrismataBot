#!/usr/bin/python3.6
class FerritinSac:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={
		"gold":1,
		"blue":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Ferritin Sac"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		self.owner.destroy(self)

	def info(self): 
		return {
		"health":self.health}

def FerritinSacCost():
	buyCostDict={
		"gold":1,
		"red":1
	}
	
	return buyCostDict,True,10,[],"Ferritin Sac"