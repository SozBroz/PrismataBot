#!/usr/bin/python3.6
class Steelsplitter:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=3
		self.fragile=False
		self.attack=1
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":1
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Steelsplitter"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self): 
		return {
		"health":self.health}

def SteelsplitterCost():
	buyCostDict={
		"gold":6,
		"blue":1
	}
	
	return buyCostDict,True,10,[],"Steelsplitter"