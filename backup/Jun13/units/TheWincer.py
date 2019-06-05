#!/usr/bin.python3.6
class TheWincer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=3
		self.defaultBlocking=False
		self.assignedBlocking=False
		self.health=5
		self.fragile=True
		self.delay=0
		self.unitsToSacrifice=[]
		self.attack=15
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":15
		}
		self.onClickCost={
		}

	def __str__(self):
		return "The Wincer"

	def startTurn(self):
		self.delay-=1
		return True

	def canClick(self):
		if self.delay>0:
			return False

		Sac=False
		multiplicity=5
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
		self.delay=3
		for unit in self.unitsToSacrifice:
			self.owner.destroy(unit)


def TheWincerCost():
	buyCostDict={
		"gold":9,
		"green":1,
		"blue":2,
		"red":1
	}
	
	return buyCostDict,True,1,[],"The Wincer"