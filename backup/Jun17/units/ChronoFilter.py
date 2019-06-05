#!/usr/bin.python3.6
class ChronoFilter:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=False
		self.health=2
		self.fragile=False
		self.delay=0
		self.attack=0
		self.startTurnDict={
		"blue":1,
		"red":1
		}

	def __str__(self):
		return "Chrono Filter"

	def startTurn(self):
		self.delay-=1
		if self.delay>0:
			return False

		self.delay=2
		return True

	def info(self):
		print("Health: "+str(self.health))
		print("Delay: "+str(self.delay))

def ChronoFilterCost():
	buyCostDict={
		"gold":4
	}
	
	return buyCostDict,False,1,[],"Chrono Filter"