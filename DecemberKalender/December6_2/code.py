tal = open("text.txt", "r").read().split(",")
tal = [int(i) for i in tal]
noll = 0
dic = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for s in tal:
   dic[s] +=1

for i in range(256):
    noll = dic[0]
    dic[0] = dic[1]
    dic[1] = dic[2]
    dic[2] = dic[3]
    dic[3] = dic[4]
    dic[4] = dic[5]
    dic[5] = dic[6]
    dic[6] = dic[7]
    dic[7] = dic[8]
    dic[8] = noll
    dic[6] +=noll
    print(dic)
print(sum(dic.values()))