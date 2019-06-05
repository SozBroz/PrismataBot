#!/usr/bin.python3.6
class VengeCannon:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=9
		self.fragile=True
		self.attack=2
		self.startTurnDict={
		"attack":2
		}
		self.onClickDict={

		}
		self.onClickCost={
		"green":4
		}

	def __str__(self):
		return "Venge Cannon"

	def startTurn(self):
		return True

	def canClick(self):
		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		if self.health<=2:
			return False

		return True

	def onClick(self):
		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		self.health-=2
		for i in range(0,3):
			owner.addUnit("Gauss Charge,1,-1")


	def info(self):
		print("Health: "+str(self.health))
		print("Fragile:",self.fragile)

def VengeCannonCost():
	buyCostDict={
		"gold":1,
		"green":3
	}
	
	return buyCostDict,True,10,['Drone', 'Drone', 'Drone'],"Venge Cannon"