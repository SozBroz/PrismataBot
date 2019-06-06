#!/usr/bin/python3.6
import sys
unitDictionary={"Nitrocybe":{"supply":20,"assignedBlocking":False,"health":1,"name":"Nitrocybe","buyCost":"1R","defaultBlocking":True,"buildTime":2,"abilityScript":{"selfSac":True,"receive":"X"}},"Pixie":{"supply":20,"assignedBlocking":False,"health":1,"name":"Pixie","buyCost":"1B","defaultBlocking":False,"buildTime":1,"abilityScript":{"selfSac":True,"receive":"X"}},"Bloodrager":{"supply":10,"startTurnScript":{"receive":"XX"},"health":2,"name":"Bloodrager","buyCost":"7RXXX","defaultBlocking":False,"buildTime":1},"Lucina Spinos":{"abilitySac":[{"multiplicity":1,"name":"Drone"}],"abilityCost":"R","supply":1,"assignedBlocking":False,"abilityScript":{"create":[{"multiplicity":1,"name":"Perforator","buildTime":1,"lifespan":-1}]},"health":1,"name":"Lucina Spinos","buyCost":"17RRRR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XXXX"}},"Cryo Ray":{"targetAmount":1,"targetAction":"chill","supply":10,"assignedBlocking":False,"healthCostToClick":1,"health":3,"name":"Cryo Ray","buyCost":"1G","defaultBlocking":False,"buildTime":1,"fragile":True},"Rhino":{"supply":10,"assignedBlocking":False,"stamina":2,"health":2,"name":"Rhino","buyCost":"5R","defaultBlocking":True,"buildTime":0,"abilityScript":{"receive":"X"},"baseSet":True},"Defense Grid":{"supply":1,"startTurnScript":{"create":[{"multiplicity":1,"name":"Drone","buildTime":1,"lifespan":-1}]},"lifespan":7,"health":7,"name":"Defense Grid","buyCost":"16BBB","defaultBlocking":True,"buildTime":1},"Iceblade Golem":{"frontline":True,"targetAction":"chill","supply":10,"assignedBlocking":False,"targetAmount":2,"health":6,"name":"Iceblade Golem","buyCost":"7BR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"X"}},"Nivo Charge":{"targetAction":"chill","supply":10,"assignedBlocking":False,"targetAmount":5,"lifespan":1,"health":1,"name":"Nivo Charge","buyCost":"2G","defaultBlocking":False,"buildTime":1,"abilityScript":{"selfSac":True}},"Scorchilla":{"supply":10,"assignedBlocking":False,"health":3,"name":"Scorchilla","buyCost":"3GR","defaultBlocking":True,"buildTime":3,"abilityScript":{"delay":3,"receive":"XXX"},"fragile":True},"Engineer":{"supply":20,"startTurnScript":{"receive":"E"},"health":1,"name":"Engineer","buyCost":"2","defaultBlocking":True,"buildTime":1,"baseSet":True},"Plexo Cell":{"buySac":[{"multiplicity":1,"name":"Drone"}],"supply":10,"lifespan":1,"health":4,"name":"Plexo Cell","buyCost":"2GG","defaultBlocking":True,"buildTime":0},"Energy Matrix":{"supply":4,"health":5,"name":"Energy Matrix","buyCost":"8BB","defaultBlocking":True,"buildTime":0},"Gauss Fabricator":{"fragile":True,"supply":1,"lifespan":8,"health":10,"name":"Gauss Fabricator","buyCost":"12GGGG","defaultBlocking":False,"buildTime":1,"startTurnScript":{"create":[{"multiplicity":1,"name":"Gauss Cannon","buildTime":1,"lifespan":-1}]}},"Chrono Filter":{"supply":1,"startTurnScript":{"delay":2,"receive":"BR"},"health":2,"name":"Chrono Filter","buyCost":"4","defaultBlocking":False,"buildTime":1},"Animus":{"supply":10,"startTurnScript":{"receive":"RR"},"health":2,"name":"Animus","buyCost":"6","defaultBlocking":False,"buildTime":1,"baseSet":True},"Thunderhead":{"frontline":True,"supply":1,"startTurnScript":{"receive":"XXXX"},"lifespan":3,"health":11,"name":"Thunderhead","buyCost":"15GGGGGB","defaultBlocking":True,"buildTime":1},"Thorium Dynamo":{"buyCost":"5E","assignedBlocking":False,"buySac":[{"multiplicity":3,"name":"Drone"}],"defaultBlocking":False,"startTurnScript":{"receive":"5G"},"fragile":True,"supply":4,"health":8,"name":"Thorium Dynamo","abilityCost":"GGG","buildTime":2,"abilityScript":{"receive":"3"}},"Vivid Drone":{"buySac":[{"multiplicity":2,"name":"Drone"}],"supply":10,"startTurnScript":{"receive":"3"},"health":1,"name":"Vivid Drone","buyCost":"2EE","defaultBlocking":False,"buildTime":1},"Synthesizer":{"abilityCost":"GGG","supply":4,"assignedBlocking":False,"abilityScript":{"receive":"BB"},"health":4,"name":"Synthesizer","buyCost":"6B","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"GG"}},"Endotherm Kit":{"spell":True,"supply":1,"buyScript":{"create":[{"multiplicity":4,"name":"Frostbite","buildTime":4,"lifespan":-1},{"multiplicity":4,"name":"Cryo Ray","buildTime":4,"lifespan":-1}]},"name":"Endotherm Kit","buyCost":"5GGGR","buildTime":0},"Frost Brooder":{"supply":4,"startTurnScript":{"create":[{"multiplicity":1,"name":"Frostbite","buildTime":1,"lifespan":3}]},"lifespan":6,"health":2,"name":"Frost Brooder","buyCost":"5RR","defaultBlocking":False,"buildTime":1},"Immolite":{"supply":20,"assignedBlocking":False,"health":1,"name":"Immolite","buyCost":"3R","defaultBlocking":True,"buildTime":1,"abilityScript":{"delay":2,"receive":"X"}},"Cynestra":{"fragile":True,"supply":4,"health":2,"name":"Cynestra","buyCost":"12GGGR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XXX"}},"Deadeye Operative":{"clickToDestroyNonblockingDrone":True,"supply":4,"assignedBlocking":False,"stamina":3,"health":2,"name":"Deadeye Operative","buyCost":"5BB","defaultBlocking":True,"buildTime":1,"abilityScript":{}},"Asteri Cannon":{"supply":4,"assignedBlocking":False,"healthCostToClick":3,"abilityScript":{"create":[{"multiplicity":1,"name":"Barrier","buildTime":0,"lifespan":-1}]},"health":16,"name":"Asteri Cannon","buyCost":"16GGGG","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XXX"},"fragile":True},"Husk":{"supply":20,"health":1,"name":"Husk","buyCost":"2R","defaultBlocking":True,"buildTime":0},"Fission Turret":{"abilityCost":"EEE","supply":10,"assignedBlocking":False,"lifespan":5,"health":1,"name":"Fission Turret","buyCost":"4G","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"X"},"abilityScript":{"selfSac":True,"receive":"GGG"}},"Arka Sodara":{"supply":1,"assignedBlocking":False,"health":7,"name":"Arka Sodara","buyCost":"7BBRXXXXXXX","defaultBlocking":True,"buildTime":0,"abilityScript":{"receive":"XXXX"}},"Auride Core":{"abilityCost":"X","supply":4,"assignedBlocking":False,"health":1,"name":"Auride Core","buyCost":"1B","defaultBlocking":False,"buildTime":1,"abilityScript":{"receive":"2"}},"Gauss Cannon":{"fragile":True,"supply":10,"health":5,"name":"Gauss Cannon","buyCost":"6G","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"X"},"baseSet":True},"Tia Thurnax":{"buySac":[{"multiplicity":7,"name":"Drone"}],"supply":1,"assignedBlocking":False,"stamina":3,"health":4,"name":"Tia Thurnax","buyCost":"7GGGR","defaultBlocking":True,"buildTime":0,"abilityScript":{"receive":"XXXXXXX"},"fragile":True},"Feral Warden":{"supply":10,"assignedBlocking":False,"health":3,"name":"Feral Warden","buyCost":"5GR","defaultBlocking":True,"buildTime":0,"abilityScript":{"receive":"X"},"fragile":True},"Mobile Animus":{"abilityCost":"3","supply":10,"assignedBlocking":False,"abilityScript":{"selfSac":True,"create":[{"multiplicity":1,"name":"Rhino","buildTime":0,"lifespan":-1}]},"health":1,"name":"Mobile Animus","buyCost":"4","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"R"}},"Zemora Voidbringer":{"abilityCost":"GGGGGGGG","supply":1,"assignedBlocking":False,"health":20,"name":"Zemora Voidbringer","buyCost":"5GGG","defaultBlocking":False,"buildTime":6,"abilityScript":{"receive":"8XXXXXXXX"},"fragile":True},"Gaussite Symbiote":{"abilityCost":"GGG","supply":4,"assignedBlocking":False,"abilityScript":{"selfSac":True,"create":[{"multiplicity":6,"name":"Gauss Charge","buildTime":1,"lifespan":-1}]},"health":2,"name":"Gaussite Symbiote","buyCost":"8RR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"GX"}},"The Wincer":{"abilitySac":[{"multiplicity":5,"name":"Drone"}],"supply":1,"assignedBlocking":False,"health":5,"name":"The Wincer","buyCost":"9GBBR","defaultBlocking":False,"buildTime":3,"abilityScript":{"delay":3,"receive":"XXXXXXXXXXXXXXX"},"fragile":True},"Perforator":{"abilityCost":"R","supply":10,"assignedBlocking":False,"health":2,"name":"Perforator","buyCost":"3R","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"X"}},"Aegis":{"fragile":True,"supply":10,"health":5,"name":"Aegis","buyCost":"6GGG","defaultBlocking":True,"buildTime":0},"Resophore":{"fragile":True,"supply":1,"attackForEach":"Forcefield","health":4,"name":"Resophore","buyCost":"1GR","defaultBlocking":False,"buildTime":5},"Blood Phage":{"abilityCost":"R","supply":4,"assignedBlocking":False,"abilityScript":{"receive":"1"},"health":2,"name":"Blood Phage","buyCost":"8ER","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"1X"}},"Barrier":{"supply":20,"lifespan":1,"health":1,"name":"Barrier","buyCost":"1G","defaultBlocking":True,"buildTime":0},"Plasmafier":{"abilitySac":[{"multiplicity":1,"name":"Drone"}],"supply":4,"assignedBlocking":False,"health":4,"name":"Plasmafier","buyCost":"12GGGB","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XXXX"},"fragile":True},"Grimbotch":{"supply":10,"assignedBlocking":False,"lifespan":4,"health":2,"name":"Grimbotch","buyCost":"4R","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"X"}},"Oxide Mixer":{"supply":4,"startTurnScript":{"create":[{"multiplicity":1,"name":"Pixie","buildTime":1,"lifespan":-1}]},"lifespan":4,"health":2,"name":"Oxide Mixer","buyCost":"3B","defaultBlocking":False,"buildTime":1},"Iso Kronus":{"fragile":True,"supply":10,"health":5,"name":"Iso Kronus","buyCost":"5G","defaultBlocking":False,"buildTime":2,"startTurnScript":{"delay":2,"receive":"XX"}},"Colossus":{"supply":4,"assignedBlocking":False,"health":8,"name":"Colossus","buyCost":"15GBBRR","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XXX"},"fragile":True},"Chieftain":{"fragile":True,"assignedBlocking":False,"lifespan":3,"health":7,"name":"Chieftain","buyCost":"8GGB","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XX"},"supply":10},"Centrifuge":{"supply":1,"startTurnScript":{"selfSac":True,"receive":"3GGBBRR"},"health":1,"name":"Centrifuge","buyCost":"5","defaultBlocking":False,"buildTime":3},"Militia":{"abilityCost":"X","supply":10,"assignedBlocking":False,"abilityScript":{"receive":"1"},"health":4,"name":"Militia","buyCost":"6B","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"X"}},"Cauterizer":{"buyScript":{"create":[{"multiplicity":4,"name":"Engineer","buildTime":1,"lifespan":-1}]},"abilityCost":"EEEE","supply":4,"assignedBlocking":False,"health":3,"name":"Cauterizer","buyCost":"11BRR","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XX"}},"Polywall":{"frontline":True,"supply":10,"health":6,"name":"Polywall","buyCost":"10B","defaultBlocking":True,"buildTime":0},"Ebb Turbine":{"abilitySac":[{"multiplicity":1,"name":"Drone"}],"supply":10,"assignedBlocking":False,"abilityScript":{"receive":"3E"},"health":4,"name":"Ebb Turbine","buyCost":"6EB","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"2"}},"Steelsplitter":{"supply":10,"assignedBlocking":False,"health":3,"name":"Steelsplitter","buyCost":"6B","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"X"},"baseSet":True},"Tatsu Nullifier":{"targetAction":"chill","supply":4,"assignedBlocking":False,"targetAmount":5,"health":2,"name":"Tatsu Nullifier","buyCost":"12RRRR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XX"}},"Auric Impulse":{"supply":20,"startTurnScript":{"selfSac":True,"receive":"4"},"health":1,"name":"Auric Impulse","buyCost":"3E","defaultBlocking":False,"buildTime":1},"Odin":{"buyScript":{"create":[{"multiplicity":3,"name":"Steelsplitter","buildTime":1,"lifespan":-1}]},"abilitySac":[{"multiplicity":1,"name":"Steelsplitter"}],"supply":1,"assignedBlocking":False,"health":4,"name":"Odin","buyCost":"20BBB","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XXXX"}},"Tarsier":{"supply":10,"startTurnScript":{"receive":"X"},"health":1,"name":"Tarsier","buyCost":"4R","defaultBlocking":False,"buildTime":2,"baseSet":True},"Kinetic Driver":{"buyCost":"5G","assignedBlocking":False,"defaultBlocking":False,"startTurnScript":{"receive":"X"},"targetAction":"snipe","supply":4,"targetCondition":{"isABC":True},"lifespan":6,"health":1,"name":"Kinetic Driver","abilityCost":"2","buildTime":1,"abilityScript":{"selfSac":True}},"Protoplasm":{"supply":10,"assignedBlocking":False,"health":4,"name":"Protoplasm","buyCost":"7GGRR","defaultBlocking":True,"buildTime":0,"abilityScript":{"selfSac":True,"receive":"XXXX"},"fragile":True},"Doomed Mech":{"supply":10,"assignedBlocking":False,"lifespan":5,"health":5,"name":"Doomed Mech","buyCost":"9BB","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XX"}},"Valkyrion":{"supply":4,"assignedBlocking":False,"health":4,"name":"Valkyrion","buyCost":"12GGBR","defaultBlocking":True,"buildTime":1,"abilityScript":{"create":[{"forOpponent":True,"name":"Barrier","multiplicity":2,"buildTime":1,"lifespan":-1}],"receive":"XXXX"}},"Vai Mauronax":{"targetAction":"chill","abilityCost":"X","supply":1,"assignedBlocking":False,"targetAmount":7,"health":6,"name":"Vai Mauronax","buyCost":"13BRRRR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XXX"}},"Conduit":{"fragile":True,"supply":10,"health":3,"name":"Conduit","buyCost":"4","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"G"},"baseSet":True},"Redeemer":{"buyScript":{"create":[{"forOpponent":True,"name":"Gauss Charge","multiplicity":6,"buildTime":3,"lifespan":-1}]},"supply":4,"assignedBlocking":False,"health":4,"name":"Redeemer","buyCost":"10GB","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XXX"}},"Infusion Grid":{"abilityCost":"R","supply":10,"assignedBlocking":False,"health":4,"name":"Infusion Grid","buyCost":"5B","defaultBlocking":True,"buildTime":1,"abilityScript":{"selfSac":True,"create":[{"multiplicity":4,"name":"Husk","buildTime":0,"lifespan":-1}]}},"Hellhound":{"buyScript":{"create":[{"multiplicity":1,"name":"Engineer","buildTime":1,"lifespan":-1}]},"supply":10,"startTurnScript":{"receive":"X"},"health":1,"name":"Hellhound","buyCost":"5BR","defaultBlocking":False,"buildTime":1},"Blood Pact":{"spell":True,"supply":10,"buyScript":{"create":[{"multiplicity":4,"name":"Husk","buildTime":0,"lifespan":-1},{"forOpponent":True,"name":"Grimbotch","multiplicity":1,"buildTime":1,"lifespan":3}]},"name":"Blood Pact","buyCost":"3R","buildTime":0},"Ossified Drone":{"name":"Ossified Drone","buyCost":"2R","assignedBlocking":False,"buySac":[{"multiplicity":1,"name":"Drone"}],"defaultBlocking":True,"startTurnScript":{"receive":"1"},"supply":1,"health":2,"abilitySac":[{"multiplicity":1,"name":"Drone"}],"abilityCost":"R","buildTime":1,"abilityScript":{"create":[{"multiplicity":1,"name":"Ossified Drone","buildTime":1,"lifespan":-1}]}},"Corpus":{"buyScript":{"create":[{"multiplicity":1,"name":"Husk","buildTime":0,"lifespan":-1}]},"abilityCost":"4R","supply":4,"assignedBlocking":False,"stamina":2,"health":2,"name":"Corpus","buyCost":"6RR","defaultBlocking":True,"buildTime":0,"abilityScript":{"create":[{"multiplicity":3,"name":"Husk","buildTime":0,"lifespan":-1}]}},"Doomed Drone":{"supply":10,"assignedBlocking":False,"lifespan":4,"health":1,"name":"Doomed Drone","buyCost":"2E","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"1"}},"Cluster Bolt":{"spell":True,"supply":10,"buyScript":{"create":[{"multiplicity":4,"name":"Gauss Charge","buildTime":1,"lifespan":-1},{"forOpponent":True,"name":"Gauss Charge","multiplicity":1,"buildTime":1,"lifespan":-1}]},"name":"Cluster Bolt","buyCost":"GGGG","buildTime":0},"Trinity Drone":{"buyCost":"2EG","assignedBlocking":False,"buySac":[{"multiplicity":2,"name":"Drone"}],"defaultBlocking":False,"startTurnScript":{"receive":"3"},"fragile":True,"supply":10,"health":5,"name":"Trinity Drone","abilityCost":"G","buildTime":1,"abilityScript":{"receive":"1"}},"Tantalum Ray":{"supply":10,"assignedBlocking":False,"healthCostToClick":3,"abilityScript":{"create":[{"multiplicity":1,"name":"Gauss Charge","buildTime":1,"lifespan":-1}]},"health":11,"name":"Tantalum Ray","buyCost":"7GG","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"X"},"fragile":True},"Drone":{"supply":20,"assignedBlocking":False,"health":1,"name":"Drone","buyCost":"3E","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"1"},"baseSet":True},"Frostbite":{"targetAction":"chill","supply":20,"assignedBlocking":False,"targetAmount":3,"health":1,"name":"Frostbite","buyCost":"2R","defaultBlocking":False,"buildTime":2,"abilityScript":{"selfSac":True}},"Manticore":{"buySac":[{"multiplicity":1,"name":"Steelsplitter"}],"supply":4,"assignedBlocking":False,"abilityCost":"XX","abilityScript":{"receive":"3"},"health":4,"name":"Manticore","buyCost":"3BB","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XX"}},"Xeno Guardian":{"supply":10,"startTurnScript":{"receive":"X"},"health":4,"name":"Xeno Guardian","buyCost":"5GBB","defaultBlocking":True,"buildTime":1},"Venge Cannon":{"buyCost":"1GGG","assignedBlocking":False,"buySac":[{"multiplicity":3,"name":"Drone"}],"defaultBlocking":False,"startTurnScript":{"receive":"XX"},"fragile":True,"supply":10,"health":9,"name":"Venge Cannon","abilityCost":"GGGG","buildTime":1,"abilityScript":{"create":[{"multiplicity":3,"name":"Gauss Charge","buildTime":1,"lifespan":-1}]},"healthCostToClick":2},"Omega Splitter":{"supply":4,"assignedBlocking":False,"health":6,"name":"Omega Splitter","buyCost":"15BBB","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XXX"}},"Thermite Core":{"abilityCost":"XX","supply":4,"assignedBlocking":False,"lifespan":5,"health":1,"name":"Thermite Core","buyCost":"1B","defaultBlocking":False,"buildTime":1,"abilityScript":{"create":[{"multiplicity":2,"name":"Pixie","buildTime":1,"lifespan":-1}]}},"Amporilla":{"supply":4,"attackForEach":"Tarsier","health":3,"name":"Amporilla","buyCost":"13RRR","defaultBlocking":False,"buildTime":1},"Centurion":{"supply":1,"startTurnScript":{"receive":"XX"},"health":6,"name":"Centurion","buyCost":"18GGBBR","defaultBlocking":True,"buildTime":0},"Grenade Mech":{"name":"Grenade Mech","buyCost":"10BB","assignedBlocking":False,"defaultBlocking":False,"startTurnScript":{"receive":"X"},"buyScript":{"create":[{"multiplicity":3,"name":"Pixie","buildTime":1,"lifespan":-1}]},"supply":4,"health":4,"abilitySac":[{"multiplicity":1,"name":"Blastforge"}],"abilityCost":"1","buildTime":1,"abilityScript":{"create":[{"multiplicity":3,"name":"Pixie","buildTime":1,"lifespan":-1}]}},"Doomed Wall":{"supply":10,"lifespan":3,"health":4,"name":"Doomed Wall","buyCost":"7B","defaultBlocking":True,"buildTime":0},"Shredder":{"frontline":True,"supply":10,"assignedBlocking":False,"health":4,"name":"Shredder","buyCost":"5B","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"X"}},"Shadowfang":{"supply":10,"startTurnScript":{"receive":"XX"},"health":1,"name":"Shadowfang","buyCost":"8RRR","defaultBlocking":False,"buildTime":1},"Electrovore":{"abilityCost":"E","supply":10,"assignedBlocking":False,"health":2,"name":"Electrovore","buyCost":"4R","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"X"}},"Gauss Charge":{"supply":20,"startTurnScript":{"selfSac":True,"receive":"X"},"health":1,"name":"Gauss Charge","buyCost":"1G","defaultBlocking":False,"buildTime":1},"Galvani Drone":{"frontline":True,"abilityCost":"E","supply":10,"assignedBlocking":False,"health":1,"name":"Galvani Drone","buyCost":"1E","defaultBlocking":False,"buildTime":1,"abilityScript":{"receive":"1"}},"Antima Comet":{"supply":1,"startTurnScript":{"selfSac":True},"attackForEach":"Engineer","health":1,"name":"Antima Comet","buyCost":"3GBR","defaultBlocking":False,"buildTime":2},"Tesla Coil":{"buyScript":{"create":[{"multiplicity":2,"name":"Engineer","buildTime":1,"lifespan":-1}]},"abilitySac":[{"multiplicity":1,"name":"Engineer"}],"supply":4,"assignedBlocking":False,"health":3,"name":"Tesla Coil","buyCost":"11GGB","defaultBlocking":False,"buildTime":1,"abilityScript":{"receive":"XXX"},"fragile":True},"Savior":{"health":4,"name":"Savior","assignedBlocking":False,"buySac":[{"multiplicity":6,"name":"Drone"}],"defaultBlocking":False,"startTurnScript":{},"supply":1,"goldForEach":"Drone","abilitySac":[{"multiplicity":1,"name":"Drone"}],"buyCost":"6","buildTime":4,"abilityScript":{"create":[{"multiplicity":1,"name":"Plasmafier","buildTime":1,"lifespan":-1}]}},"Wall":{"supply":10,"health":3,"name":"Wall","buyCost":"5B","defaultBlocking":True,"buildTime":0,"baseSet":True},"Mahar Rectifier":{"healthGained":2,"assignedBlocking":False,"supply":10,"health":5,"name":"Mahar Rectifier","buyCost":"11GG","defaultBlocking":True,"buildTime":1,"abilityScript":{"receive":"XX"},"fragile":True},"Lancetooth":{"supply":10,"assignedBlocking":False,"health":4,"name":"Lancetooth","buyCost":"6BXX","defaultBlocking":True,"buildTime":2,"abilityScript":{"receive":"XX"}},"Xaetron":{"healthGained":4,"assignedBlocking":False,"supply":1,"healthCostToClick":7,"health":4,"name":"Xaetron","buyCost":"11GGGGG","defaultBlocking":True,"buildTime":0,"abilityScript":{"create":[{"multiplicity":5,"name":"Gauss Charge","buildTime":1,"lifespan":-1}]},"fragile":True},"Arms Race":{"spell":True,"supply":4,"buyScript":{"create":[{"multiplicity":1,"name":"Tarsier","buildTime":2,"lifespan":-1},{"multiplicity":1,"name":"Gauss Cannon","buildTime":1,"lifespan":-1},{"multiplicity":1,"name":"Steelsplitter","buildTime":1,"lifespan":-1},{"forOpponent":True,"name":"Engineer","multiplicity":4,"buildTime":1,"lifespan":-1}]},"name":"Arms Race","buyCost":"8GBR","buildTime":0},"Blastforge":{"supply":10,"startTurnScript":{"receive":"B"},"health":3,"name":"Blastforge","buyCost":"5","defaultBlocking":False,"buildTime":1,"baseSet":True},"Steelforge":{"name":"Steelforge","buyCost":"4","assignedBlocking":False,"buySac":[{"multiplicity":1,"name":"Blastforge"}],"defaultBlocking":False,"startTurnScript":{"receive":"BB"},"supply":4,"health":4,"abilitySac":[{"multiplicity":1,"name":"Drone"}],"abilityCost":"1BB","buildTime":1,"abilityScript":{"create":[{"multiplicity":1,"name":"Steelsplitter","buildTime":1,"lifespan":-1}]}},"Wild Drone":{"frontline":True,"supply":4,"startTurnScript":{"receive":"2"},"health":3,"name":"Wild Drone","buyCost":"5EE","defaultBlocking":False,"buildTime":1},"Forcefield":{"buySac":[{"multiplicity":1,"name":"Drone"}],"fragile":True,"supply":20,"health":2,"name":"Forcefield","buyCost":"1G","defaultBlocking":True,"buildTime":0,"baseSet":True},"Shiver Yeti":{"targetAction":"chill","supply":10,"assignedBlocking":False,"targetAmount":2,"health":2,"name":"Shiver Yeti","buyCost":"5R","defaultBlocking":True,"buildTime":0},"Tyranno Smorcus":{"abilityCost":"RR","supply":4,"assignedBlocking":False,"abilityScript":{"receive":"X"},"health":2,"name":"Tyranno Smorcus","buyCost":"5RR","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"X"}},"Drake":{"abilitySac":[{"multiplicity":1,"name":"Blastforge"}],"supply":4,"assignedBlocking":False,"abilityScript":{"receive":"XX"},"health":4,"name":"Drake","buyCost":"12BB","defaultBlocking":False,"buildTime":1,"startTurnScript":{"receive":"XX"}},"Apollo":{"targetAction":"snipe","supply":1,"assignedBlocking":False,"targetCondition":{"healthAtMost":3},"health":4,"name":"Apollo","buyCost":"13BBB","defaultBlocking":False,"buildTime":2},"Hannibull":{"frontline":True,"supply":4,"assignedBlocking":False,"abilityScript":{"receive":"X"},"health":7,"name":"Hannibull","buyCost":"10BR","defaultBlocking":True,"buildTime":1,"startTurnScript":{"receive":"X"}},"Borehole Patroller":{"buyScript":{"create":[{"multiplicity":1,"name":"Pixie","buildTime":1,"lifespan":-1}]},"supply":10,"startTurnScript":{"receive":"X"},"health":2,"name":"Borehole Patroller","buyCost":"6GB","defaultBlocking":True,"buildTime":1},"Urban Sentry":{"supply":10,"startTurnScript":{"receive":"X"},"health":3,"name":"Urban Sentry","buyCost":"5GB","defaultBlocking":True,"buildTime":1},"Sentinel":{"supply":10,"assignedBlocking":False,"stamina":3,"health":4,"name":"Sentinel","buyCost":"7GR","defaultBlocking":True,"buildTime":1,"abilityScript":{"create":[{"multiplicity":1,"name":"Engineer","buildTime":1,"lifespan":-1}],"receive":"X"},"fragile":True},"Flame Animus":{"supply":4,"startTurnScript":{"receive":"RX"},"health":2,"name":"Flame Animus","buyCost":"5B","defaultBlocking":False,"buildTime":2},"Ferritin Sac":{"supply":10,"assignedBlocking":False,"health":1,"name":"Ferritin Sac","buyCost":"1R","defaultBlocking":False,"buildTime":2,"abilityScript":{"selfSac":True,"receive":"1B"}}}
unitDictionary["GunbotForge"]={"supply":10,"buildTime":1,"buyCost":"G","health":4,"name":"Gunbot Forge","startTurnScript":{"create":[{"multiplicity":1,"name":"Gunbot","buildTime":1,"lifespan":-1}]}}
unitDictionary["Gunbot"]={"supply":0,"buildTime":1,"buyCost":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","health":1,"name":"Gunbot","startTurnScript":{"receive":"X"}}
unitDictionary["Tough Fabricator"]={"supply":0,"buildTime":1,"buyCost":"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG","health":20,"name":"Tough Fabricator","startTurnScript":{"create":[{"multiplicity":1,"name":"Steelsplitter","buildTime":1,"lifespan":-1}]}}
unitDictionary["Assembler"]={"supply":0,"buildTime":1,"buyCost":"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG","health":4,"name":"Assembler","startTurnScript":{"create":[{"multiplicity":1,"name":"Steelsplitter","buildTime":1,"lifespan":-1}]}}
unitDictionary["Litterbug"]={"supply":0,"health":1,"name":"Litterbug","buyCost":"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG","buildTime":0}
counter=0
baseSetList=[]

def cleanNameFunc(name):
	cleanName=""
	for i in name.split(" "):
		cleanName+=i
	name=cleanName
	cleanName=""
	for i in name.split("'"):
		cleanName+=name
	name=cleanName
	cleanName=""
	for i in name.split("."):
		cleanName+=i
	return(cleanName)

def buyCostDictAppend(val1,val2):
	global buyCostDict
	for i in range(0,len(val1)):
		if len(buyCostDict)>1:
			buyCostDict.append((",\n\t\t\""+str(val1[i])+"\""+":"+str(val2[i])))
		else:
			buyCostDict.append(("\t\t\""+str(val1[i])+"\""+":"+str(val2[i])))

def onClickDictAppend(val1,val2):
	global onClickDict
	for i in range(0,len(val1)):
		if len(onClickDict)>1:
			onClickDict.append((",\n\t\t\""+str(val1[i])+"\""+":"+str(val2[i])))
		else:
			onClickDict.append(("\t\t\""+str(val1[i])+"\""+":"+str(val2[i])))

def startTurnDictAppend(val1,val2):
	global startTurnDict
	for i in range(0,len(val1)):
		if len(startTurnDict)>1:
			startTurnDict.append((",\n\t\t\""+str(val1[i])+"\""+":"+str(val2[i])))
		else:
			startTurnDict.append(("\t\t\""+str(val1[i])+"\""+":"+str(val2[i])))

def shortHandToResource(shortHand):
	resource=[]
	resourceCount=[]
	skip=0
	try:
		int(shortHand[0])
		resource.append("gold")
		skip=1
		
		try:
			int(shortHand[1])
			skip=2
			resourceCount.append(int(str(shortHand[0])+str(shortHand[1])))

		except (ValueError, IndexError):
			resourceCount.append(shortHand[0])

	except ValueError:
		pass

	for i in range(skip,len(shortHand)):
		if shortHand[i]=="X":
			if "attack" in resource:
				resourceCount[resource.index("attack")]+=1
			else:
				resource.append("attack")
				resourceCount.append(1)

		elif shortHand[i]=="R":
			if "red" in resource:
				resourceCount[resource.index("red")]+=1
			else:
				resource.append("red")
				resourceCount.append(1)

		elif shortHand[i]=="B":
			if "blue" in resource:
				resourceCount[resource.index("blue")]+=1
			else:
				resource.append("blue")
				resourceCount.append(1)

		elif shortHand[i]=="G":
			if "green" in resource:
				resourceCount[resource.index("green")]+=1
			else:
				resource.append("green")
				resourceCount.append(1)

		elif shortHand[i]=="E":
			if "energy" in resource:
				resourceCount[resource.index("energy")]+=1
			else:
				resource.append("energy")
				resourceCount.append(1)
		else:
			print(shortHand)
			sys.exit("UNKNOWN resource AT shortHandToResource")

	return (resource, resourceCount)

scriptAttributeList=["selfSac","receive","create","delay"]
targetActionAttributeList=["chill","snipe"]

for i in unitDictionary:
	attackValue=0
	unitOnClickBoolean=False
	temp=unitDictionary[i] #turn back to i
	print(temp)
	cleanName=cleanNameFunc(i) #turn back to i
	if 'baseSet' in temp and temp['baseSet']==True:
		baseSetList.append(cleanName)
		temp.pop('baseSet')
	priority=[]
	lastPriority=[]
	afterChecks=[]
	STpriority=[]
	STlastPriority=[]
	STafterChecks=[]
	
	print(cleanName)
	print(temp)
		
	startTurnScript=["\n\n\tdef startTurn(self):"]
	infoScript=["\n\n\tdef info(self): \n\t\treturn {"]
	onClickScript=["\n\n\tdef onClick(self):"]
	onClickDict=["\n\t\tself.onClickDict={\n"]
	startTurnDict=["\n\t\tself.startTurnDict={\n"]
	onClickCost=["\n\t\tself.onClickCost={"]
	unitFile=open(("units/"+cleanName+".py"),"w")
	unitFile.write(("#!/usr/bin/python3.6\nclass "+cleanName+":\n\tdef __init__(self,owner):"))
	isSpell=False
	if "spell" in temp and temp["spell"]==True:
		isSpell=True
		temp.pop("spell")
		for attribute in scriptAttributeList:
			if attribute in temp['buyScript']:
				try:
					if attribute=="create":
						for index in range(0,len(temp["buyScript"]["create"])):
							if 'forOpponent' not in temp["buyScript"]["create"][0]:
								print(index)
								unitFile.write(("\n\t\tfor i in range(0,"+str(temp["buyScript"]["create"][0]["multiplicity"])+"):"))
								unitFile.write(("\n\t\t\towner.addUnit(\""+temp["buyScript"]["create"][0]["name"]+","+str(temp["buyScript"]["create"][0]["buildTime"])+","+str(temp["buyScript"]["create"][0]["lifespan"])+"\")\n"))
								temp["buyScript"]["create"][0].pop('multiplicity')
								temp["buyScript"]["create"][0].pop('name')
								temp["buyScript"]["create"][0].pop('buildTime')
								temp["buyScript"]["create"][0].pop('lifespan')
							else:
								unitFile.write(("\n\t\tfor i in range(0,"+str(temp["buyScript"]["create"][0]["multiplicity"])+"):"))
								unitFile.write(("\n\t\t\towner.opponent.addUnit(\""+temp["buyScript"]["create"][0]["name"]+","+str(temp["buyScript"]["create"][0]["buildTime"])+","+str(temp["buyScript"]["create"][0]["lifespan"])+"\")\n"))
								temp["buyScript"]["create"][0].pop('multiplicity')
								temp["buyScript"]["create"][0].pop('name')
								temp["buyScript"]["create"][0].pop('buildTime')
								temp["buyScript"]["create"][0].pop('lifespan')
								temp["buyScript"]["create"][0].pop('forOpponent')
							
							if len(temp["buyScript"]["create"][0])==0:
								temp["buyScript"]["create"]=temp["buyScript"]["create"][1:]
							else:
								print("unknown buyScript create")
								print("index:",index)
								print(temp["buyScript"]["create"])
								sys.exit(0)
						if len(temp['buyScript']['create'])==0:
							temp['buyScript'].pop('create')

						else:
							print("unkown buyScript create value")
							print(temp['buyScript']['create'])
							sys.exit()

				except IndexError:
					print("Spell keyError")
					print(temp)
					print(sys.exit(0))

		unitFile.write("\n\t\tself.cooldown="+str(temp["buildTime"]))
		unitFile.write("\n\t\towner.destroy(self)")
		temp.pop("buildTime")


		if len(temp["buyScript"])>0:
			print("UNKNOWN buyscript attribute")
			print(buyScript)
			sys.exit(0)

		temp.pop("buyScript")
		unitFile.write(("\n\n\tdef __str__(self):\n\t\treturn \""+temp['name']+"\""))
		fullName=temp["name"]
		temp.pop('name')


	else: #not script
		unitFile.write("\n\t\tself.owner=owner")
		if 'lifespan' in temp:
			infoScript.append("\n\t\t\"lifespan\":self.lifespan")
			unitFile.write("\n\t\tself.lifespan="+str(temp['lifespan']))
			temp.pop('lifespan')
		else:
			unitFile.write("\n\t\tself.lifespan=-1")

		if 'frontline' in temp:
			infoScript.append("\n\t\t\"frontline\":self.frontline")
			unitFile.write("\n\t\tself.frontline="+str(temp['frontline']))
			temp.pop('frontline')
		else:
			unitFile.write("\n\t\tself.frontline=False")
		if 'stamina' in temp:
			infoScript.append("\n\t\t\"stamina\":self.stamina")
			unitFile.write("\n\t\tself.stamina="+str(temp['stamina']))
			priority.append("\n\t\tif self.stamina==0:")
			priority.append("\n\t\t\treturn False\n")
			afterChecks.append("\n\t\tself.stamina-=1")
			temp.pop('stamina')
		else:
			print("no stamina")

		if "buyScript" in temp:
			for attribute in scriptAttributeList:
				if attribute in temp["buyScript"]:
					if attribute=="create":
						for toBeCreated in temp["buyScript"]["create"]:
							unitFile.write(("\n\t\tfor i in range(0,"+str(toBeCreated["multiplicity"])+"):"))
							unitFile.write(("\n\t\t\tself.owner.addUnit(\""+toBeCreated["name"]+","+str(toBeCreated["buildTime"])+","+str(toBeCreated["lifespan"])+"\")\n"))
					
						temp['buyScript'].pop('create')

			if len(temp["buyScript"])>0:
				print("UNKNOWN initialize buyScript option")
				print(temp)
				sys.exit(0)
			else:
				temp.pop('buyScript')

		try:
			unitFile.write(("\n\t\tself.cooldown="+str(temp['buildTime'])))
			temp.pop('buildTime')

		except KeyError:
			print("No buildTime")

		try:
			unitFile.write(("\n\t\tself.defaultBlocking="+str(temp['defaultBlocking'])))
			temp.pop('defaultBlocking')

		except KeyError:
			print("no defaultBlocking")

		try: 
			unitFile.write(("\n\t\tself.assignedBlocking="+str(temp['assignedBlocking'])))
			temp.pop('assignedBlocking')

		except KeyError:
			print("no assignedBlocking")


		print(temp)
		unitFile.write(("\n\t\tself.health="+str(temp['health'])))
		infoScript.append("\n\t\t\"health\":self.health")
		if temp['health']>1:
			if 'fragile' in temp:
				infoScript.append("\n\t\t\"fragile\":self.fragile")
				unitFile.write("\n\t\tself.fragile="+str(temp['fragile']))
				temp.pop('fragile')
				if 'healthGained' in temp:
					if cleanName=="Xaetron":
						startTurnScript.append('\n\t\tself.maxHealth=12')
						startTurnScript.append("\n\t\tself.health=min(self.health+"+str(temp["healthGained"])+",self.maxHealth)")
						temp.pop('healthGained')
					else:
						startTurnScript.append('\n\t\tself.initHealth='+str(temp['health']))
						startTurnScript.append("\n\t\tself.health=min(self.health+"+str(temp["healthGained"])+",self.initHealth)")
						temp.pop('healthGained')
			else:
				unitFile.write("\n\t\tself.fragile=False")
		temp.pop('health')

		
		
		try:
			for attribute in scriptAttributeList:
				if attribute in temp["abilityScript"]:
					if attribute=="receive":
						t1,t2=shortHandToResource(temp["abilityScript"]["receive"])
						onClickDictAppend(t1,t2)
						if "attack" in t1:
							attackValue+=t2[t1.index("attack")]
						temp["abilityScript"].pop('receive')

					elif attribute=="selfSac":
						afterChecks.append("\n\t\tself.owner.destroy(self)")
						temp["abilityScript"].pop('selfSac')

					elif attribute=="create":
						for index in range(0,len(temp["abilityScript"]["create"])):
							if 'forOpponent' in temp["abilityScript"]["create"][0]:
								lastPriority.append(("\n\t\tfor i in range(0,"+str(temp["abilityScript"]["create"][0]["multiplicity"])+"):"))
								lastPriority.append(("\n\t\t\towner.opponent.addUnit(\""+temp["abilityScript"]["create"][0]["name"]+","+str(temp["abilityScript"]["create"][0]["buildTime"])+","+str(temp["abilityScript"]["create"][0]["lifespan"])+"\")\n"))
								temp["abilityScript"]["create"][0].pop("multiplicity")
								temp["abilityScript"]["create"][0].pop("name")
								temp["abilityScript"]["create"][0].pop("buildTime")
								temp["abilityScript"]["create"][0].pop("lifespan")
								temp["abilityScript"]["create"][0].pop("forOpponent")
							else:
								lastPriority.append(("\n\t\tfor i in range(0,"+str(temp["abilityScript"]["create"][0]["multiplicity"])+"):"))
								lastPriority.append(("\n\t\t\towner.addUnit(\""+temp["abilityScript"]["create"][0]["name"]+","+str(temp["abilityScript"]["create"][0]["buildTime"])+","+str(temp["abilityScript"]["create"][0]["lifespan"])+"\")\n"))
								temp["abilityScript"]["create"][0].pop("multiplicity")
								temp["abilityScript"]["create"][0].pop("name")
								temp["abilityScript"]["create"][0].pop("buildTime")
								temp["abilityScript"]["create"][0].pop("lifespan")

						if len(temp["abilityScript"]["create"][0])>0:
							print("unknown variable in ability script create")
							sys.exit()
						else:
							temp["abilityScript"]["create"]=temp["abilityScript"]["create"][1:]

						temp["abilityScript"].pop('create')

					elif attribute=="delay":
						infoScript.append("\n\t\t\"delay\":self.delay")
						unitFile.write("\n\t\tself.delay=0")
						startTurnScript.append("\n\t\tself.delay-=1")
						priority.append("\n\t\tif self.delay>0:")
						priority.append("\n\t\t\treturn False\n")
						afterChecks.append("\n\t\tself.delay="+str(temp["abilityScript"]["delay"]))
						temp["abilityScript"].pop("delay")



			if len(temp["abilityScript"])>0:
				print("temp[abilityScript]")
				print(temp["abilityScript"])
				sys.exit("UNKNOWN attribute")
			else:
				temp.pop('abilityScript')

		except KeyError:
			print(temp)
			print("abilityScript KeyError")
			pass #no abilityScript

		if 'attackForEach' in temp:

			STpriority.append("\n\t\tself.owner.resDict[\"attack\"]+=self.owner.numberOfUnit(\""+temp['attackForEach']+"\")")
			temp.pop('attackForEach')

		if 'goldForEach' in temp:
			STpriority.append("\n\t\tself.owner.resDict[\"gold\"]+=self.owner.numberOfUnit(\""+temp['goldForEach']+"\")")
			temp.pop('goldForEach')

		if "clickToDestroyNonblockingDrone" in temp:
			priority.append("\n\t\tcanSnipeBoolean=False")
			priority.append("\n\t\tfor unit in self.owner.opponent.masterList:")
			priority.append("\n\t\t\tif str(unit)==\"Drone\":")
			priority.append("\n\t\t\t\tif unit not in self.owner.opponent.blockers:")
			priority.append("\n\t\t\t\t\tcanSnipeBoolean=True")
			priority.append("\n\t\t\t\t\tbreak\n")
			priority.append("\n\t\tif canSnipeBoolean==False:")
			priority.append("\n\t\t\treturn False\n")
			afterChecks.append("\n\t\tself.owner.snipe(\"Drone\")")
			temp.pop("clickToDestroyNonblockingDrone")

		if "abilitySac" in temp:
			unitFile.write('\n\t\tself.unitsToSacrifice=[]')
			priority.append(("\n\t\tSac=False"))
			for toBeSacrificed in temp["abilitySac"]:
				priority.append(("\n\t\tmultiplicity="+str(toBeSacrificed["multiplicity"])))
				priority.append(("\n\t\tself.unitsToSacrifice=[]"))
				priority.append(("\n\t\tfor unit in owner.unitsListWithOnClick:"))
				priority.append(("\n\t\t\tif str(unit)==\""+toBeSacrificed["name"]+"\":"))
				priority.append(("\n\t\t\t\tself.unitsToSacrifice.append(unit)"))
				priority.append(("\n\t\t\t\tif len(self.unitsToSacrifice)==multiplicity:"))
				priority.append(("\n\t\t\t\t\tbreak\n\t\t\t\t\tSac=True\n"))
			
			priority.append("\n\t\tif Sac == False:")
			priority.append("\n\t\t\treturn False\n")
			afterChecks.append(("\n\t\tfor unit in self.unitsToSacrifice:"))
			afterChecks.append(("\n\t\t\tself.owner.destroy(unit)\n"))
			temp.pop("abilitySac")

		if "abilityCost" in temp:
			t1,t2=shortHandToResource(temp["abilityCost"])
			for i in range(0,(len(t1)-1)):
				onClickCost.append(("\n\t\t"+t1[i]+":"+str(t2[i])+","))
			onClickCost.append(("\n\t\t\""+t1[-1]+"\":"+str(t2[-1])))
			priority.append(("\n\t\tfor i in self.OnClickCost"))
			priority.append(("\n\t\t\tif owner.resDict[i]<=onClickCost:"))
			priority.append(("\n\t\t\t\treturn False\n"))
			afterChecks.append(("\n\t\tfor i in self.onClickCost:"))
			afterChecks.append(("\n\t\t\tplayer.resDict[i]-=self.onClickCost[i]\n"))

			temp.pop("abilityCost")

		try:
			for attribute in scriptAttributeList:
				if attribute in temp["startTurnScript"]:
					if attribute=="receive":
						t1,t2=shortHandToResource(temp["startTurnScript"]["receive"])
						startTurnDictAppend(t1,t2)
						if "attack" in t1:
							attackValue+=t2[t1.index("attack")]
						temp["startTurnScript"].pop('receive')

					elif attribute=="selfSac":
						STlastPriority.append("\n\t\tself.owner.destroy(self)")
						temp["startTurnScript"].pop('selfSac')

					elif attribute=="create":
						for toBeCreated in temp["startTurnScript"]["create"]:
							STlastPriority.append(("\n\t\tfor i in range(0,"+str(toBeCreated["multiplicity"])+"):"))
							STlastPriority.append(("\n\t\t\tself.owner.addUnit(\""+toBeCreated["name"]+","+str(toBeCreated["buildTime"])+","+str(toBeCreated["lifespan"])+"\")\n"))
						temp["startTurnScript"].pop('create')

					elif attribute=="delay":
						infoScript.append("\n\t\t\"delay\":self.delay")
						unitFile.write("\n\t\tself.delay=0")
						STpriority.append("\n\t\tself.delay-=1")
						STpriority.append("\n\t\tif self.delay>0:")
						STpriority.append("\n\t\t\treturn False\n")
						STafterChecks.append("\n\t\tself.delay="+str(temp["startTurnScript"]["delay"]))
						temp["startTurnScript"].pop("delay")

			if len(temp["startTurnScript"])>0:
				print("temp[startTurnScript]")
				print(temp["startTurnScript"])
				sys.exit("UNKOWN attribute")
			else:
				temp.pop('startTurnScript')

		except KeyError:
			print("KeyError StartTurnScript")
			print("attribute:",attribute)
			print("temp:",temp)
			print("startTurnScript:",startTurnScript)
			pass 

		if 'healthCostToClick' in temp:
			priority.append("\n\t\tif self.health<="+str(temp["healthCostToClick"])+":")
			priority.append("\n\t\t\treturn False\n")
			afterChecks.append("\n\t\tself.health-="+str(temp["healthCostToClick"]))
			temp.pop('healthCostToClick')

		else:
			print("no healthCostToClick")

		if 'targetAction' in temp:
			for attribute in targetActionAttributeList:
				if temp['targetAction']==attribute:
					if attribute=='chill':
						afterChecks.append("\n\t\tself.owner.freeze("+str(temp["targetAmount"])+")")
						temp.pop('targetAction')
						temp.pop('targetAmount')
						break

					elif attribute=='snipe':
							targetConditions=[]
							for a in temp['targetCondition']:
								targetConditions.append(a)
							priority.append("\n\t\tif not self.owner.canSnipe("+str(targetConditions)+")")
							priority.append("\n\t\t\treturn False\n")
							afterChecks.append("\n\t\tself.owner.snipe("+str(targetConditions)+")")
							temp.pop('targetAction')
							temp.pop('targetCondition')
							break

					else:
						print("unknown targetAction")
						print(temp)
						sys.exit(0)

		else:
			print("No TargetAction")
		unitFile.write(("\n\t\tself.attack="+str(attackValue)))
		for i in startTurnDict:
			unitFile.write(i)
		unitFile.write("\n\t\t}")

		if len(onClickScript+priority+afterChecks+lastPriority)>1 or len(onClickDict)>1 or len(onClickCost)>1:
			for i in onClickDict:
				unitFile.write(i)

			unitFile.write("\n\t\t}")
			for i in onClickCost:
				unitFile.write(i)

			unitFile.write("\n\t\t}")
			unitOnClickBoolean=True

		unitFile.write(("\n\n\tdef __str__(self):\n\t\treturn \""+temp['name']+"\""))
		fullName=temp["name"]
		temp.pop('name')
		unitFile.write(startTurnScript[0])
		for line in STpriority+startTurnScript[1:]+STafterChecks+STlastPriority:
			unitFile.write(line)

		unitFile.write("\n\t\treturn True")

		if len(onClickScript+priority+afterChecks+lastPriority)>1 or len(onClickDict)>1 or len(onClickCost)>1:
			unitFile.write("\n\n\tdef canClick(self):")
			for line in priority:
				unitFile.write(line)
			unitFile.write("\n\t\treturn True")
			unitFile.write(onClickScript[0])
			# for line in priority:
			# 	unitFile.write(line)
			# for line in onClickScript[1:]:
			# 	unitFile.write(line)
			if len(afterChecks+lastPriority)==0:
				unitFile.write("\n\t\tpass")
			else:
				for line in afterChecks:
					unitFile.write(line)
				for line in lastPriority:
					unitFile.write(line)


			unitOnClickBoolean=True
		if len(infoScript)>1:
			unitFile.write(infoScript[0])
			if len(infoScript)==2:
				unitFile.write(infoScript[1])

			else:
				for line in infoScript[1:-1]:
					unitFile.write((line+","))

				unitFile.write(infoScript[-1])

			unitFile.write("}")
		else:
			pass

	counter+=1
	buyCostDict=["\n\ndef "+cleanName+"Cost():\n\tbuyCostDict={\n"]
	t1,t2=shortHandToResource(temp['buyCost'])
	buyCostDictAppend(t1,t2)
	temp.pop('buyCost')
	for i in buyCostDict:
		unitFile.write(i)

	unitFile.write("\n\t}")
	buySacList=[]
	if "buySac" in temp:
		for toBeSacrificed in temp["buySac"]:
			for multiplicity in range(0,toBeSacrificed["multiplicity"]):
				buySacList.append(toBeSacrificed["name"])
		temp.pop("buySac")
	if not isSpell:
		unitFile.write(("\n\t\n\treturn buyCostDict,"+str(unitOnClickBoolean)+","+str(temp['supply'])+","+str(buySacList)+",\""+fullName+"\""))
	else:
		unitFile.write(("\n\t\n\treturn buyCostDict,"+"\"Spell\""+","+str(temp['supply'])+","+str(buySacList)+",\""+fullName+"\""))

	temp.pop("supply")
	if len(temp)>0:
		print("temp not empty")
		print(temp)
		sys.exit()
	#if counter>0:
	#	sys.exit()


baseSetFile=open("units/BaseSetList","w")
for i in range(0,len(baseSetList)-1):
	baseSetFile.write((baseSetList[i]+","))

baseSetFile.write(baseSetList[-1])
