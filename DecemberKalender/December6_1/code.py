tal = open("text.txt", "r").read().split(",")
tal = [int(i) for i in tal]


for i in range(80):

    for idx,s in enumerate(tal):
        if s == 0:
            tal.append(9)
            tal[idx]=6    
        else:
            tal[idx]-=1

    print("{} / 256, ({:1f}%), {} lanternfishes".format(i, (i / 265 * 100), len(tal)))
print(len(tal))