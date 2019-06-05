#!/usr/bin.python3.6
class FlameAnimus:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=2
		self.defaultBlocking=False
		self.health=2
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"red":1,
		"attack":1
		}

	def __str__(self):
		return "Flame Animus"

	def startTurn(self):
		return True

def FlameAnimusCost():
	buyCostDict={
		"gold":5,
		"blue":1
	}
	
	return buyCostDict,False,4,[],"Flame Animus"