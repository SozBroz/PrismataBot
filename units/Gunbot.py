#!/usr/bin/python3.6
class Gunbot:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.health=1
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Gunbot"

	def startTurn(self):
		return True

	def info(self): 
		return {
		"health":self.health}

def GunbotCost():
	buyCostDict={
		"attack":71
	}
	
	return buyCostDict,False,0,[],"Gunbot"