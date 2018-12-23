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

answerSet = []
answerNum = []
answerWeight = []
answerStart = []
probiblty = 2
for number in range(1000):
    newMwis = []
    noChange = []
    for i in range(n):
        newMwis.append(random.randint(1, 300)%2) #init everyone is random in newMwis
        noChange.append(0) #append each process changed
    
    while True: # to do round
        doCount = 0
        oldMwis = newMwis.copy()
        for i in range(n):   #each process to do
            k = random.randint(1, 10)   
            if k <= probiblty:
                continue
            doCount += 1
            
            for j, connect in enumerate(neighbor[i]): #every process receive from neighbor
                if connect == 1:
                    if oldMwis[j] == 1:
                        if weight[j] > weight[i]:
                            newMwis[i] = 0
                            break
                        elif weight[j] == weight[i]: #if equal weight, not compare id
                            newMwis[i] = 0
                            break
                newMwis[i] = 1
            
            if oldMwis[i] == newMwis[i]:
                noChange[i] = 1


            

        #end choose mwis

        finish = True
        for i in range(n):
            if oldMwis[i] != newMwis[i]: #compare old and new
                noChange[i] = 0
                for j, connect in enumerate(neighbor[i]):
                    if connect:
                        noChange[j] = 0
        if sum(noChange) == n and doCount >0:
            break

    answer = []
    total = 0
    for i, b in enumerate(newMwis):
        if b == 1:
            answer.append(i)
            total += oriWeight[i]
    '''
    print("MWIS : ", sorted(answer))
    print("Total weight: ",total)
    '''


    if sorted(answer) not in answerSet:
        answerSet.append(sorted(answer))
        answerNum.append(1)
        answerWeight.append(total)
    else:
        index = answerSet.index(sorted(answer))
        answerNum[index] += 1


for i, ansSet in enumerate(answerSet):
    if ansSet == [0]:
        print("Infinite no answer percentage:", (answerNum[i]/1000)*100,"%")
    else:
        print("set: ", ansSet," total weight:",answerWeight[i]," percentage:",(answerNum[i]/1000)*100,"%")
print("\n")