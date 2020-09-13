#cidades = []

#n = int(input("Numero de cidades: "))
#for i in range(1, n+1):
#    cidades.append(int(input()))
dist1 = {}
dist2 = {}
caminho = []
caminho2 = []
j = 1
cidades = [7, 3, 9, 5, 3, 7, 5, 2, 6, 1, 10, 11, 9]
for n in cidades:
    dist1["c" + str(j)] = n
    j += 1

print(dist1)

for k, v in dist1.items():
    k = k.replace("c", ""); dist2["d"+k+"."+str(v)] = 1

print(dist2)

def dist(a, b, second = False):
    if a == b:
        print(caminho, caminho2)
        return 0
    


    if "d"+str(a)+"."+str(b) in dist2:
        print("d"+str(a)+"."+str(b))
        if second is False:
            caminho.append(a)
            print(caminho)
        if second is True:
            caminho2.append(a)
            print(len(caminho) - len(caminho2))
        

    else:
        for num in range(1, len(cidades)+1):     
            if "d"+str(a)+"."+str(num) in dist2:
                print("d"+str(a)+"."+str(num))
                
                if a in caminho and second is False:
                    break
                if a in caminho2 and second is True:
                    break
                if a in caminho and second is True:
                    print(a, num)
                    caminho2.append(a)
                    caminho2.append(num)
                    print(caminho, caminho2)
                    if caminho.index(a) < caminho2.index(a):
                        print(caminho.index(a) + 1)
                    else:
                        print(caminho2.index(a) + 1)
                    raise SystemExit

                if second is False:
                    caminho.append(a)
                    print(caminho, caminho2)
                    return dist(num, b)
                if second is True:
                    caminho2.append(a)
                    return dist(num, b, True)
                print(caminho, caminho2)
                   

    return "Fim"

x1 = int(input())
x2 = int(input())


print(dist(x1, x2))   
print(dist(x2, x1, True))   
