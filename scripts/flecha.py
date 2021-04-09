import time

def dist(x,y):
    x = int(x); y = int(y)
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    
    return x + y

#programa principal
distancia = []
checker = 0
n = int(input())
for i in range(n):
    x_y = input().split(" ")
    distancia.append(dist(x_y[0], x_y[1]))

set_time = time.time()
for i in range(len(distancia)):
    for j in range(i+1, len(distancia)):
        if distancia[i] <= distancia[j]:
            checker += 1

print(checker)