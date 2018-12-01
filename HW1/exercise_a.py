import sys


f = open(sys.argv[1], "r")
n = int(f.readline()) #n node

nodes = f.readline()
nodeWeight = {}
originWeight = []
adjMatrix = []
for i in range(n):
    tmp = []
    line = f.readline()
    for j in line.split():
        tmp.append(int(j))
    adjMatrix.append(tmp)
f.close()

for i, weight in enumerate(nodes.split()):
    originWeight.append(int(weight))
    weight = int(weight)/sum(adjMatrix[i])
    nodeWeight[i] = weight



answer = []
total = 0
while len(nodeWeight) > 0:
    temp = sorted(nodeWeight.items(), key=lambda d: d[0], reverse = True) #Let large id to sorted last
    temp = sorted(temp, key = lambda d: d[1])
    ansTemp = temp.pop()
    total += originWeight[ansTemp[0]]
    del nodeWeight[ansTemp[0]]
    for i, connect in enumerate(adjMatrix[ansTemp[0]]):
        if connect == 1 and nodeWeight.get(i) != None:
            del nodeWeight[i]
    answer.append(ansTemp[0]) 
    
#print(adjMatrix)
print("MWIS : ", end='')
print(sorted(answer))
print("Total weight: ",total)

