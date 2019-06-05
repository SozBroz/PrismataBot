#!/usr/bin/python3.6
class Shredder:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=True
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
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
		return "Shredder"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self): 
		return {
		"frontline":self.frontline,
		"health":self.health}

def ShredderCost():
	buyCostDict={
		"gold":5,
		"blue":1
	}
	
	return buyCostDict,True,10,[],"Shredder"