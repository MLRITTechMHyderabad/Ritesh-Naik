d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]

li=[]
for i in d1:
    for j in d2:
        li.append((i,j))

print(li)

sums=[]
for tup in li:
    result=sum(tup)
    sums.append(result)

print(sums)

count={}

for i in range(2,13):
    count[i]=sums.count(i)/len(li)

print(count)


userinput= input("enter the numbers")
listOfInput=userinput.split()
P1_d1 = int(listOfInput[0])
P1_d2 = int(listOfInput[1])
P2_d1 = int(listOfInput[2])
P2_d2 = int(listOfInput[3])

P1_sum = P1_d1 + P1_d2
P2_sum = P2_d1 + P2_d2

def getResult(P1_sum,P2_sum):
    if count[P1_sum]>count[P2_sum] :
        print("Player 2 won")
    elif count[P2_sum] > count[P1_sum]:
        print("Player 1 won")
    else:
        print("Draw")

getResult(P1_sum,P2_sum)

