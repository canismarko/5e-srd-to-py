import os
import shelve

inf = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "local_data", "monsters.shlf")
outf = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "output_files", "monsters.py")

header = """\"\"\"
monsters.py

A collection of monsters from D&D 5e's SRD
\"\"\"

"""

individual_class = \
'''

class {classname}(Monster):
    """{description}

    {attacks}

    """

    name = "{name}"
    description = "{size} {type}, {alignment}"
    challenge_rating = {challenge_rating}
    armor_class = {armor_class}
    skills = "{skills}"
    senses = "{senses}"
    languages = "{languages}"
    strength = Ability({strength})
    dexterity = Ability({dexterity})
    constitution = Ability({constitution})
    intelligence = Ability({intelligence})
    wisdom = Ability({wisdom})
    charisma = Ability({charisma})
    speed = {speed_walk}
    swim_speed = {speed_swim}
    fly_speed = {speed_fly}
    hp_max = {hit_points}
    hit_dice = "{hit_dice}"

'''

def get_attacks(monster_data):
    """
    Returns a string list of attacks for the monster

    :param monster_data:
    :return:
    """
    return ""
    # TODO: Write me!

def get_skills(monster_data):
    """
    Returns a string list of skills for the monster

    :param monster_data:
    :return:
    """
    return ""
    # TODO: Write me!

def get_monster_string(monster_data):
    data = monster_data
    data["classname"] = "".join(monster_data["name"].split())
    data["description"] = ""
    data["attacks"] = get_attacks(monster_data)
    data["skills"] = get_skills(monster_data)
    data["speed_walk"] = monster_data["speed"].get("walk", "0")
    data["speed_swim"] = monster_data["speed"].get("swim", "0")
    data["speed_fly"] = monster_data["speed"].get("fly", "0")

    ret = (individual_class.format(**data))
    print(ret)
    return ret

def write_monsters():
    with shelve.open(inf, 'r') as db:
        outstr = header
        for monster in db["data"]:
            monster_string = get_monster_string(monster)
            outstr += monster_string
    with open(outf, 'w') as f:
        f.write(outstr)


if __name__ == '__main__':
    write_monsters()
