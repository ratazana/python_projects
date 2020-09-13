from itertools import product
lists = []

k_m = [int(i) for i in input().split(" ")]
k = k_m[0]
m = k_m[1]

for i in range(k):
    aux = [int(i) for i in input().split(" ")]
    lists.append(aux[1:])


S = map(lambda x: sum(i**2 for i in x)%m,product(*lists))

print(max(S))


