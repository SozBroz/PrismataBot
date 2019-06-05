Robust as far as I can tell - Should catch and whine about all rule breaking commands
Currently has only been tested for basic set
Im sure there are some other units that will work if you want to uncomment the prompt for additional units.  Units with snipe and freeze definitely wont work.

Engine.py is what you run to start the game - was written for python3.6
Unit names are capitalized
Commands:
if in squared brackets than optional
Info:
i for info
i defaults to information on all units owned by both players.
You must provided options in order, you can't get info on all Drones from both players for example.

attempts to return information on the unit (health, lifespan, stamina, if can be clicked, if is currently blocking)
0/1 for player 1/2
UnitName can be cleaned up name with no spaces or full name
unit# can specify which index of the selected unit you want info on

i [0|1] [unitName] [unit#]

Buy:
b for buy - attempts to buy a unit
UnitName can be cleaned up name with no spaces or full name
#ofunits  defaults to 1 if not provided

b unitName [#ofunits]

Click:
c for info - attempts to click a unit
UnitName can be cleaned up name with no spaces or full name
unit# can specify which index of the selected unit you want to click - defaults to every unit

c unitName [unit#]


Attack:
a Enters attack phase - ends buy/click/info phase

a

During Attack Phase:
Intended for blocker to choose blockers if they have more defensive strength than the opponents attacking strength

If attacking strength is greater than it automatically destroys all blockers (breaches) and attacker gets to choose what to attack
UnitName can be cleaned up name with no spaces or full name - unit to take damage next
unit# can specify which unit takes damage - defaults to first found unit with the unitName provided.

unitName [unit#]