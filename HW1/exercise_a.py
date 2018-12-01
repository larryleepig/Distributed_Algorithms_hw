import sys

f = open(sys.argv[1], "r")
n = int(f.readline()) #n node

nodes = f.readline()
nodeWeight = []


print(nodeWeight)

adjMatrix = []
for i in range(n):
    tmp = []
    line = f.readline()
    for j in line.split():
        tmp.append(j)
    adjMatrix.append(tmp)

for i, weight in enumerate(nodes.split()):
    weight = int(weight)/sum(adjMatrix[i])
    nodeWeight.append((i, weight))

print(nodeWeight) 
    
#print(adjMatrix)

f.close()
