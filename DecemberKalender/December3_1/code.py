bi=open("text.txt", "r").read().splitlines()
x=0
tal = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,  
}

for i in range(12):
    for s in bi:
        if s[i] == "1":
            tal[i] += 1

for i in range(12):
    if tal[i] > 500:
        tal.pop(i)
        tal[i]=1
    else:
        tal.pop(i)
        tal[i]=0

copy = tal.copy()
for i in range(12):
    if copy[i]== 0:
        copy[i]=1
    else:
        copy[i]=0
gamma="".join([str(i) for i in copy.values()])
epsilon="".join([str(i) for i in tal.values()])
gamma=int(gamma, base=2)
epsilon=int(epsilon, base=2)
svar=gamma*epsilon
print(svar)