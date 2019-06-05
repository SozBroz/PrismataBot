#!/usr/bin.python3.6
class Apollo:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Apollo"

	def startTurn(self):
		return True

	def canClick(self):
		if not self.owner.canSnipe(['healthAtMost'])
			return False

		return True

	def onClick(self):
		self.owner.snipe(['healthAtMost'])

def ApolloCost():
	buyCostDict={
		"gold":13,
		"blue":3
	}
	
	return buyCostDict,True,1,[],"Apollo"