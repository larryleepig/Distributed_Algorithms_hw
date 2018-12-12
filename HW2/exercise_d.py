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
    for i in range(n):
        newMwis.append(random.randint(1, 300)%2) #init everyone is random in newMwis
    finish = False
    wrongAnswer = True
    while True: # to do round
        if finish and not wrongAnswer: #if wrongAnswer happen , not stopping loop 
            break
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
                            if oldMwis[i] == 1:
                                wrongAnswer = True #simulate broadcast wrongAnswer
                            newMwis[i] = random.randint(1, 300)%2 #random decide in or out
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
    print("set: ", ansSet," total weight:",answerWeight[i]," percentage:",(answerNum[i]/1000)*100,"%")
print("\n")