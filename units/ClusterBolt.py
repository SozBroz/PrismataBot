#!/usr/bin/python3.6
class ClusterBolt:
	def __init__(self,owner):
		for i in range(0,4):
			owner.addUnit("Gauss Charge,1,-1")

		for i in range(0,1):
			owner.opponent.addUnit("Gauss Charge,1,-1")

		self.cooldown=0
		owner.destroy(self)

	def __str__(self):
		return "Cluster Bolt"

def ClusterBoltCost():
	buyCostDict={
		"green":4
	}
	
	return buyCostDict,"Spell",10,[],"Cluster Bolt"