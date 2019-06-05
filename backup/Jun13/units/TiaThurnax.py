#!/usr/bin.python3.6
class TiaThurnax:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.stamina=3
		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=True
		self.attack=7
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":7
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Tia Thurnax"

	def startTurn(self):
		return True

	def canClick(self):
		if self.stamina==0:
			return False
		return True

	def onClick(self):
		self.stamina-=1

def TiaThurnaxCost():
	buyCostDict={
		"gold":7,
		"green":3,
		"red":1
	}
	
	return buyCostDict,True,1,['Drone', 'Drone', 'Drone', 'Drone', 'Drone', 'Drone', 'Drone'],"Tia Thurnax"