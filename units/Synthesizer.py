#!/usr/bin/python3.6
class Synthesizer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=0
		self.startTurnDict={
		"green":2
		}
		self.onClickDict={
		"blue":2
		}
		self.onClickCost={
		"green":3
		}

	def __str__(self):
		return "Synthesizer"

	def startTurn(self):
		return True

	def canClick(self):
		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]


	def info(self): 
		return {
		"health":self.health}

def SynthesizerCost():
	buyCostDict={
		"gold":6,
		"blue":1
	}
	
	return buyCostDict,True,4,[],"Synthesizer"