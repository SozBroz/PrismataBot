#!/usr/bin/python3.6
class GunbotForge:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.health=4
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Gunbot Forge"

	def startTurn(self):
		for i in range(0,1):
			self.owner.addUnit("Gunbot,1,-1")

		return True

	def info(self): 
		return {
		"health":self.health}

def GunbotForgeCost():
	buyCostDict={
		"green":1
	}
	
	return buyCostDict,False,10,[],"Gunbot Forge"