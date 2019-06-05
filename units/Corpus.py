#!/usr/bin/python3.6
class Corpus:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.stamina=2
		for i in range(0,1):
			self.owner.addUnit("Husk,0,-1")

		self.cooldown=0
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		gold:4,
		"red":1
		}

	def __str__(self):
		return "Corpus"

	def startTurn(self):
		return True

	def canClick(self):
		if self.stamina==0:
			return False

		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		self.stamina-=1
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,3):
			owner.addUnit("Husk,0,-1")


	def info(self): 
		return {
		"stamina":self.stamina,
		"health":self.health}

def CorpusCost():
	buyCostDict={
		"gold":6,
		"red":2
	}
	
	return buyCostDict,True,4,[],"Corpus"