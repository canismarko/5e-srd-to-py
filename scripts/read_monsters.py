import requests
import shelve
import os

# This takes a good 2ish minutes to run. I didn't time it though

base_url = "https://www.dnd5eapi.co"
outf = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "local_data", "monsters.shlf")

def make_monsters_list():
    monsters_list = requests.get(base_url+"/api/monsters").json()
    urls = [monster['url'] for monster in monsters_list['results']]
    monsters = []
    for url in urls:
        endpoint = base_url + url
        monster = requests.get(endpoint).json()
        monsters.append(monster)
    shelf = shelve.open(outf)
    shelf["data"] = monsters
    shelf.close()


if __name__ == '__main__':
    make_monsters_list()