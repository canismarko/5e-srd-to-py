import os
import shelve

inf = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "local_data", "monsters.shlf")
outf = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "output_files", "monsters.py")

header = """\"\"\"
monsters.py

A collection of monsters from D&D 5e's SRD
\"\"\"

"""

def write_monsters():
    with shelve.open(inf, 'r') as db:
        for l in db["data"]:
            print(l)  # It's working!

if __name__ == '__main__':
    write_monsters()
