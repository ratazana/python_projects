entrada = input().split(" ")
n = int(entrada[0])
m = int(entrada[1])
l = int(entrada[2])
r = int(entrada[3])


distancias = []
resultados = 0


for i in range(int(n)):
    for j in range(int(m)):
        distancias.append([i, j])

def distancia(ponto1, ponto2):
    return ((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)**0.5

for i in range(len(distancias)):
    for j in range(i+1, len(distancias)):
        if distancias[i][1] == distancias[j][1] and distancias[i][0] - distancias[j][0] not in range(-1, 2) \
        or distancias[i][0] == distancias[j][0] and distancias[i][1] - distancias[j][1] not in range(-1, 2) \
        or abs(distancias[i][1] - distancias[j][1]) == abs(distancias[i][0] - distancias[j][0]) and distancias[i][0] - distancias[j][0] not in range(-1, 2) \
        or abs(distancias[i][1] - distancias[j][1]) == abs(distancias[i][0] - distancias[j][0]) and distancias[i][1] - distancias[j][1] not in range(-1, 2) :
            continue
        
        else: 
            if distancia(distancias[i], distancias[j]) <= r and distancia(distancias[i], distancias[j]) >= l:
                resultados += 1
        
print(resultados % ((10**9)+7))