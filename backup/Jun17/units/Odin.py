#!/usr/bin.python3.6
class Odin:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		for i in range(0,3):
			owner.player.addUnit("Steelsplitter,1,-1")

		self.cooldown=1
		self.defaultBlocking=True
		self.assignedBlocking=False
		self.health=4
		self.fragile=False
		self.unitsToSacrifice=[]
		self.attack=4
		self.startTurnDict={

		}
		self.onClickDict={
		"attack":4
		}
		self.onClickCost={
		}

	def __str__(self):
		return "Odin"

	def startTurn(self):
		return True

	def canClick(self):
		Sac=False
		multiplicity=1
		self.unitsToSacrifice=[]
		for unit in owner.unitsListWithOnClick:
			if str(unit)=="Steelsplitter":
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


	def info(self):
		print("Health: "+str(self.health))

def OdinCost():
	buyCostDict={
		"gold":20,
		"blue":3
	}
	
	return buyCostDict,True,1,[],"Odin"