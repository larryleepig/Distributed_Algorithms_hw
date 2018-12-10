import sys
import random

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
    weight.append(int(w)/(sum(neighbor[i]) + 1))
    oriWeight.append(int(w))
f.close()

newMwis = []
for i in range(n):
    newMwis.append(random.randint(1, 300)%2) #init everyone is random in newMwis 

#print(newMwis)

while True: # to do round
    oldMwis = newMwis.copy()
    wrongAnswer = False
    for i in range(n):   #each process to do       
        for j, connect in enumerate(neighbor[i]): #every process receive from neighbor
            if connect == 1:
                if oldMwis[j] == 1:
                    if weight[j] > weight[i]:
                        newMwis[i] = 0
                        break
                    elif weight[j] == weight[i]:
                        newMwis[i] = (random.randint(1, 300) % 2
                        if oldMwis[i] == 1:
                            wrongAnswer = True
                        break
                    else:
                        newMwis[i] = 1
                else:
                    newMwis[i] = 1
            else: #if there are not connect must be chose itself
                newMwis[i] = 1
    #end choose mwis
    finish = True
    for i in range(n):
        if oldMwis[i] != newMwis[i]: #compare old and new
            finish = False
            break
    if finish and not wrongAnswer:
        break

answer = []
total = 0
for i, b in enumerate(newMwis):
    if b == 1:
        answer.append(i)
        total += oriWeight[i]

print("MWIS : ", sorted(answer))
print("Total weight: ",total)
