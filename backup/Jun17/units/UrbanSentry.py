#!/usr/bin.python3.6
class UrbanSentry:
	def __init__(self,owner):
		self.owner=owner
		self.lifespan=-1
		self.frontline=False
		self.cooldown=1
		self.defaultBlocking=True
		self.health=3
		self.fragile=False
		self.attack=1
		self.startTurnDict={
		"attack":1
		}

	def __str__(self):
		return "Urban Sentry"

	def startTurn(self):
		return True

	def info(self):
		print("Health: "+str(self.health))

def UrbanSentryCost():
	buyCostDict={
		"gold":5,
		"green":1,
		"blue":1
	}
	
	return buyCostDict,False,10,[],"Urban Sentry"