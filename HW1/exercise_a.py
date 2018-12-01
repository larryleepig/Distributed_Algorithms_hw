import sys

f = open(sys.argv[1], "r")
n = f.readline() #n node

nodes = f.readline()
nodeWeight = []

for i in nodes.split():
    nodeWeight.append(i)
print(nodeWeight)

adjMatrix = []
for i in range(n):
    tmp = []
    line = f.readline()
    for j in line.split():
        tmp.append(j)
    adjMatrix.append(tmp)

print(adjMatrix)

f.close()
