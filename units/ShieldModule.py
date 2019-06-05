#!/usr/bin/python3.6
class ShieldModule:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=0
		self.defaultBlocking=True
		self.health=1
		self.fragile=False
		self.attack=0
		self.startTurnDict={

		}

	def __str__(self):
		return "Shield Module"

	def startTurn(self):
		return True

	def info(self):
		return {"health":self.health}

def ShieldModuleCost():
	buyCostDict={
		"gold":3,
		"blue":1
	}
	
	return buyCostDict,False,0,[],"Shield Module"