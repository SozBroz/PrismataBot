#!/usr/bin.python3.6
class OssifiedDrone:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=2
		self.fragile=False
		self.unitsToSacrifice=[]
		self.attack=0
		self.startTurnDict={
		"gold":1
		}
		self.onClickDict={

		}
		self.onClickCost={
		"red":1
		}

	def __str__(self):
		return "Ossified Drone"

	def startTurn(self):
		return True

	def canClick(self):
		Sac=False
		multiplicity=1
		self.unitsToSacrifice=[]
		for unit in owner.unitsListWithOnClick:
			if str(unit)=="Drone":
				self.unitsToSacrifice.append(unit)
				if len(self.unitsToSacrifice)==multiplicity:
					break
					Sac=True

		if Sac == False:
			return False

		for i in self.OnClickCost
			if owner.resDict[i]<=onClickCost:
				return False

		return True

	def onClick(self):
		for unit in self.unitsToSacrifice:
			self.owner.destroy(unit)

		for i in self.onClickCost:
			player.resDict[i]-=self.onClickCost[i]

		for i in range(0,1):
			owner.addUnit("Ossified Drone,1,-1")


def OssifiedDroneCost():
	buyCostDict={
		"gold":2,
		"red":1
	}
	
	return buyCostDict,True,1,['Drone'],"Ossified Drone"