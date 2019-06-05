#!/usr/bin.python3.6
class Savior:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=4
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.unitsToSacrifice=[]
		self.attack=0
		self.startTurnDict={

		}
		self.onClickDict={

		}
		self.onClickCost={
		}

	def __str__(self):
		return "Savior"

	def startTurn(self):
		self.owner.resDict["gold"]+=self.owner.numberOfUnit("Drone")
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

		return True

	def onClick(self):
		for unit in self.unitsToSacrifice:
			self.owner.destroy(unit)

		for i in range(0,1):
			owner.addUnit("Plasmafier,1,-1")


	def info(self):
		print("Health: "+str(self.health))

def SaviorCost():
	buyCostDict={
		"gold":6
	}
	
	return buyCostDict,True,1,['Drone', 'Drone', 'Drone', 'Drone', 'Drone', 'Drone'],"Savior"