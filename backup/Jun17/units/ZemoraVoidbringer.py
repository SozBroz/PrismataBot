#!/usr/bin.python3.6
class ZemoraVoidbringer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=6
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=20
		self.fragile=True
		self.attack=8
		self.startTurnDict={

		}
		self.onClickDict={
		"gold":8,
		"attack":8
		}
		self.onClickCost={
		"green":8
		}

	def __str__(self):
		return "Zemora Voidbringer"

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
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def ZemoraVoidbringerCost():
	buyCostDict={
		"gold":5,
		"green":3
	}
	
	return buyCostDict,True,1,[],"Zemora Voidbringer"