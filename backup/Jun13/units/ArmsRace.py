#!/usr/bin.python3.6
class ArmsRace:
	def __init__(self,owner):
		for i in range(0,1):
			owner.addUnit("Tarsier,2,-1")

		for i in range(0,1):
			owner.addUnit("Gauss Cannon,1,-1")

		for i in range(0,1):
			owner.addUnit("Steelsplitter,1,-1")

		for i in range(0,4):
			owner.opponent.addUnit("Engineer,1,-1")

		self.cooldown=0
		owner.destroy(self)

	def __str__(self):
		return "Arms Race"

def ArmsRaceCost():
	buyCostDict={
		"gold":8,
		"green":1,
		"blue":1,
		"red":1
	}
	
	return buyCostDict,"Spell",4,[],"Arms Race"