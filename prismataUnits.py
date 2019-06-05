#!/usr/bin/python3.6
class Engineer:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=1
		self.owner=owner
			
	def __str__(self):
		return "Engineer" 

	def startTurn(self):
		self.owner.resDict["energy"]+=1
		self.owner.resDict["defence"]+=self.hp

class Drone:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=1
		self.owner=owner
		self.onClickDict={
		"defence":-self.hp,
		"gold":1
		}
		self.onClickResCostDict={
		}
	def __str__(self):
		return "Drone"	

	def startTurn(self):
		self.owner.resDict["defence"]+=self.hp
		
	def onClick(self):
		self.cooldown=-1
			#print("owner gold:",self.owner.resDict["gold"])
		#print("cooldown:",self.cooldown)

class Animus:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=2
		self.owner=owner

	def __str__(self):
		return "Animus"

	def startTurn(self):
		self.owner.resDict["red"]+=2
		
class Tarsier:
	def __init__(self,owner):
		self.owner=owner
		self.cooldown=-2
		self.hp=1

	def __str__(self):
		return "Tarsier"

	def startTurn(self):
		self.owner.resDict["attack"]+=1

class Immolite:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=1
		self.owner=owner
		self.onClickDict={
		"defence":-self.hp,
		"attack":1
		}
		self.onClickResCostDict={
		}

	def __str__(self):
		return "Immolite"

	def startTurn(self):
		self.owner.resDict["defence"]+=self.hp

	def onClick(self):
		self.cooldown=-2
			
class Perforator:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=2
		self.owner=owner
		self.attackValue=1
		self.onClickDict={
		"defence":-self.hp,
		"attack":self.attackValue,
		}
		self.onClickResCostDict={
		"red":1
		}

	def __str__(self):
		return "Perforator"

	def startTurn(self):
		self.owner.resDict["defence"]+=self.hp

	def onClick(self):
		self.cooldown=-1
			
class Shadowfang:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=1
		self.owner=owner
		self.attackValue=2

	def __str__(self):
		return "Shadowfang"

	def startTurn(self):
		self.owner.resDict["attack"]+=self.attackValue

class Nitrocybe:
	def __init__(self,owner):
		self.cooldown=-2
		self.hp=1
		self.owner=owner
		self.onClickDict={
		'attack':1,
		'defence':-self.hp
		}
		self.onClickResCostDict={
		}
		
	def __str__(self):
		return "Nitrocybe"

	def startTurn(self):
		self.owner.resDict["defence"]+=self.hp

	def onClick(self):
		index=self.owner.otherUnitsClick.index(self)
		self.owner.otherUnitsClick=self.owner.otherUnitsClick[:index]+self.owner.otherUnitsClick[index+1:]

class Wall:
	def __init__(self,owner):
		self.cooldown=0
		self.hp=3
		self.owner=owner

	def __str__(self):
		return "Wall"

	def startTurn(self):
		self.owner.defence+=self.hp

class ShieldModule:
	def __init__(self,owner):
		self.cooldown=0
		self.hp=1
		self.owner=owner

	def __str__(self):
		return "Shield Module"

	def startTurn(self):
		self.owner.defence+=self.hp

class Blastforge:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=3
		self.owner=owner

	def __str__(self):
		return "Blastforge"

	def startTurn(self):
		self.owner.resDict["blue"]+=1

class FlameAnimus:
	def __init__(self,owner):
		self.cooldown=-2
		self.hp=2
		self.owner=owner

	def __str__(self):
		return "Flame Animus"

	def startTurn(self):
		self.owner.resDict["red"]+=1
		self.owner.resDict["attack"]+=1

class GunbotForge:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=4
		self.owner=owner
		self.onClickDict={}
		self.onClickResCostDict={
		}
	def __str__(self):
		return "Gunbot Forge"

	def startTurn(self):
		pass

	def onClick(self):
		self.owner.otherUnitsClick.append(Gunbot(self.owner))
		self.cooldown=-1

class Gunbot:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=1
		self.owner=owner
		self.onClickDict={
		"attack":1
		}
		self.onClickResCostDict={
		}
	def __str__(self):
		return "Gunbot"

	def startTurn(self):
		pass

	def onClick(self):
		self.cooldown=-1

class ToughFabricator:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=20
		self.owner=owner
		self.hpIncrementer=6

	def __str__(self):
		return "Tough Fab"

	def startTurn(self):
		self.owner.otherUnitsClick.append(ToughGunbot)
		self.owner.otherUnitsClick[-1].hp=hpIncrementer
		self.hpIncrementer+=1

class ToughGunbot:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=3
		self.owner=owner
		self.onClickDict={
		"attack":1
		}
		self.onClickResCostDict={
		}

	def __str__(self):
		return "Tough Gunbot"

	def startTurn(self):
		pass

	def onClick(self):
		self.cooldown=-1

class ExoStructor:
	def __init__(self,owner):
		self.cooldown=-1
		self.hp=8
		self.owner=owner
		self.patternTracker=0

	def __str__(self):
		return "Exo Structor"

	def startTurn(self):
		temp=patternTracker%3
		if temp==0:
			self.owner.otherUnitsClick.append(GunbotForge)
		elif temp==1:
			self.owner.otherUnits.append(ShieldModule)
			self.owner.otherUnits.append(Wall)
		elif temp==2:
			self.append.otherUnitsClick.append(Gunbot)
