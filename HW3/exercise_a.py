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


for number in range(1000):
    newMwis = []
    noChange = []
    for i in range(n):
        newMwis.append(random.randint(1, 300)%2) #init everyone is random in newMwis
        noChange.append(0)  #append each process changed
    
    while True: # to do round
        oldMwis = newMwis.copy()
        '''
        if oldMwis not in decideRecord:
            decideRecord.append(oldMwis)
            loopnum = 0
        else:
            loopnum += 1
            if loopnum > len(decideRecord)*1000:
                infinite = True
                break
        '''
        i = random.randint(0, (n-1)) #random decide process i
        #print(noChange)
        #for i in range(n):   #each process to do       
        for j, connect in enumerate(neighbor[i]): #every process receive from neighbor
            if connect == 1:
                if oldMwis[j] == 1:
                    if weight[j] > weight[i]:
                        newMwis[i] = 0
                        break
                    elif weight[j] == weight[i]: #if equal weight, not compare id
                        newMwis[i] = 0
                        break
                    else:
                        newMwis[i] = 1
                else:
                    newMwis[i] = 1
            else: #if there are not connect must be chose itself
                newMwis[i] = 1
        
        if oldMwis[i] == newMwis[i]:
            noChange[i] = 1
        else:
            noChange[i] = 0 #if self change should tell neighbor need to decide again
            for j , connect in enumerate(neighbor[i]):
                if connect:
                    noChange[j] = 0
        #end choose mwis
        if sum(noChange) == n:
            break

    answer = []
    total = 0
    for i, b in enumerate(newMwis):
        if b == 1:
            answer.append(i)
            total += oriWeight[i]

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