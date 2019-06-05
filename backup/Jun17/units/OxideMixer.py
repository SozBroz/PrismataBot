#!/usr/bin.python3.6
class OxideMixer:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=4
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=2
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Oxide Mixer"

	def startTurn(self):
		for i in range(0,1):
			owner.player.addUnit("Pixie,1,-1")

		return True

	def info(self):
		print("Lifespan: "+str(self.lifespan))
		print("Health: "+str(self.health))

def OxideMixerCost():
	buyCostDict={
		"gold":3,
		"blue":1
	}
	
	return buyCostDict,False,4,[],"Oxide Mixer"