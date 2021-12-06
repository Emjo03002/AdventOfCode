tal=0
tal=open("tal.txt", "r").read().splitlines()
tal_list=[int(i) for i in tal]
print(tal_list)
item=0
increased=0

while item!=1999:
    if tal_list[item]<tal_list[item+1]:
        increased +=1
        item+=1
    else:
        item+=1

print(increased)