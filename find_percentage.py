times = int(input())
score = []
mean = 0

for i in range(times):
    data = [i for i in input().split(" ")]
    score.append(data)
    
goal = input()
for i in range(times):
    if score[i][0] == goal:
        for j in range(1, 4):
            mean += float(score[i][j])

print(f'{mean/3:.2f}')

