#!/usr/bin.python3.6
class EndothermKit:
	def __init__(self,owner):
		for i in range(0,4):
			owner.addUnit("Frostbite,4,-1")

		for i in range(0,4):
			owner.addUnit("Cryo Ray,4,-1")

		self.cooldown=0
		owner.destroy(self)

	def __str__(self):
		return "Endotherm Kit"

def EndothermKitCost():
	buyCostDict={
		"gold":5,
		"green":3,
		"red":1
	}
	
	return buyCostDict,"Spell",1,[],"Endotherm Kit"