import sys

sys.path.append('../')

from iso4217 import Currency as cur
from random import choice
import os

from data_structures.double_hashing_hash_map import DoubleHashingHashMap
from definitions import ROOT_DIR

codes = [currency.code for currency in cur]

N = 10_000

z = int(sys.argv[1])
num_collision = []

for i in range(N):
    print(f"{z}: {i + 1}/{N}")
    my_map = DoubleHashingHashMap(z=z)
    # 70 insertions
    for _ in range(70):
        my_map[choice(codes)] = "value"
    # 30 deletions
    for _ in range(30):
        try:
            del my_map[choice(codes)]
        except KeyError:
            pass
    num_collision.append(my_map.get_collisions())

result = {z: sum(num_collision)/N}
with open(os.path.join(ROOT_DIR, 'resources', f'collisions_{z}.txt'), "w") as f:
    f.write(str(result) + "\n")
