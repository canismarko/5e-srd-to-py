# 5e-srd-to-py
Parse JSON, CSV, etc. representations of 5e documents into python code for use in other projects

## Recognition
This makes extensive use of https://www.dnd5eapi.co/api/. Contribute
to their project portfolio in https://github.com/5e-bits. 

## Running this Program

You will need to have `requests` to run the `read_` scripts which
use the 5e API.

The general flow of this tool is:

1. Run one of the `read_` scripts to get some data from a CSV file or the 5e API
2. Run the corresponding `write_` script that reads the `shelf` file written by the `read` script to create a python script
3. Include the auto-generated python script into the library you want.

### Read Scripts

Scripts that start with `read_` are meant to read the
5e API or CSV files and create python `shelf` objects that are stored in `local_data`.

### Write Scripts

Scripts that start with `write_` are meant to read the `shelf` objects
(used to minimize hits to the database) and create Python
classes that can be used with other programs like `dungeon-sheets`.

An example output is the `monsters.py` which, from the 5e API will generate code like:

```python

class AncientRedDragon(Monster):
    """
    **Multiattack**: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.

    **Bite**: Melee Weapon Attack: +17 to hit, reach 15 ft., one target. Hit: 21 (2d10 + 10) piercing damage plus 14 (4d6) fire damage.

    **Claw**: Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 17 (2d6 + 10) slashing damage.

    **Tail**: Melee Weapon Attack: +17 to hit, reach 20 ft., one target. Hit: 19 (2d8 + 10) bludgeoning damage.

    **Frightful Presence**: Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.

    **Fire Breath**: The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.


    """

    name = "Ancient Red Dragon"
    description = "Gargantuan dragon, chaotic evil"
    challenge_rating = 24
    armor_class = 22
    skills = "Perception +16, Stealth +7"
    senses = "Blindsight 60 ft., Darkvision 120 ft., Passive Perception 26"
    languages = "Common, Draconic"
    strength = Ability(30)
    dexterity = Ability(10)
    constitution = Ability(29)
    intelligence = Ability(18)
    wisdom = Ability(15)
    charisma = Ability(23)
    speed = 40
    swim_speed = 0
    fly_speed = 80
    climb_speed = 40
    hp_max = 546
    hit_dice = "28d20"

```

## Contributing

This is sort of a pet project to make some useful python code to put into other projects. Namely dungeon-sheets
and dungeon-encounters. If you want to add some code, cool! Make a pull request. Generally the intention of *this*
project is to get a bunch of data from something like a csv file or the 5e SRD API and make it into a python class
for other projects

