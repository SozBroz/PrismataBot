#!/usr/bin.python3.6
class BloodPact:
	def __init__(self,owner):
		for i in range(0,4):
			owner.addUnit("Husk,0,-1")

		for i in range(0,1):
			owner.opponent.addUnit("Grimbotch,1,3")

		self.cooldown=0
		owner.destroy(self)

	def __str__(self):
		return "Blood Pact"

def BloodPactCost():
	buyCostDict={
		"gold":3,
		"red":1
	}
	
	return buyCostDict,"Spell",10,[],"Blood Pact"