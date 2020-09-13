from random import randint
from operator import itemgetter

dices = {"Player a": randint(1,6), 
         "Player b": randint(1,6),
         "Player c": randint(1,6),
         "Player d": randint(1,6)}
ranking = {}
ranking = sorted(dices.items(), key=itemgetter(1), reverse=True)
for k, v in dices.items():
    print(f'{k} got {v}.')

print("Ranking: ")

for i in ranking:
    print(f'{i[0]} got {i[1]}')