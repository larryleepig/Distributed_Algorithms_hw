import sys


f = open(sys.argv[1], "r")
n = int(f.readline()) #n node

nodes = f.readline()

  
neighbor = []
for i in range(n):
    tmp = []
    line = f.readline()
    for j in line.split():
        tmp.append(int(j))
    neighbor.append(tmp)

weight = []
oriWeight = []  
for i, w in enumerate(nodes.split()):
    weight.append(int(w)/sum(neighbor[i]))
    oriWeight.append(int(w))
f.close()

newMwis = []
for i in range(n):
    newMwis.append(0) #init everyone is not in Mwisn

round = 0
while True: # to do round
    oldMwis = []
    for i in range(n):
        oldMwis.append(newMwis[i])
    for i in range(n):
        for j, connect in enumerate(neighbor[i]):
            if connect == 1:
                if oldMwis[j] == 1:
                    if weight[j] > weight[i]:
                        newMwis[i] = 0
                        break
                    elif weight[j] == weight[i] and j < i:
                        newMwis[i] = 0
                        break
                    else:
                        newMwis[i] = 1
                else:
                    newMwis[i] = 1
    finish = True
    round += 1
    for i in range(n):
        if oldMwis[i] != newMwis[i]:
            finish = False
            break
    if finish:
        break

answer = []
total = 0
for i, b in enumerate(newMwis):
    if b == 1:
        answer.append(i)
        total += oriWeight[i]

print("MWIS : ", end='')
print(sorted(answer))
print("Total weight: ",total)

