#!/usr/bin.python3.6
class AuricImpulse:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=1
		self.attack=0
		self.startTurnDict={
		"gold":4
		}

	def __str__(self):
		return "Auric Impulse"

	def startTurn(self):
		self.owner.destroy(self)
		return True

def AuricImpulseCost():
	buyCostDict={
		"gold":3,
		"energy":1
	}
	
	return buyCostDict,False,20,[],"Auric Impulse"