#!/usr/bin.python3.6
class OmegaSplitter:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=6
		self.fragile=False
		self.attack=3
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":3
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Omega Splitter"

	def startTurn(self):
		return True

	def canClick(self):
		return True

	def onClick(self):
		pass

	def info(self):
		print("Health: "+str(self.health))

def OmegaSplitterCost():
	buyCostDict={
		"gold":15,
		"blue":3
	}
	
	return buyCostDict,True,4,[],"Omega Splitter"