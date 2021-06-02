import requests
import shelve
import os

header = """\"\"\"
monsters.py

A collection of monsters from D&D 5e's SRD
\"\"\"

"""

base_url = "https://www.dnd5eapi.co"
outf = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "output_files", "monsters.shlf")

def make_monsters_list():
    monsters_list = requests.get(base_url+"/api/monsters").json()
    urls = [monster['url'] for monster in monsters_list['results']]
    monsters = []
    for url in urls[0:3]:
        endpoint = base_url + url
        monster = requests.get(endpoint).json()
        monsters.append(monster)
    print(outf)

if __name__ == '__main__':
    make_monsters_list()