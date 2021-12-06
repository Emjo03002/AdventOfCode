tal=open("tal.txt", "r").read().splitlines()
tal_list=[int(i) for i in tal]

item=0
increased=0

while item!=len(tal_list)-3:
    if tal_list[item]+tal_list[item+1]+tal_list[item+2]<tal_list[item+1]+tal_list[item+2]+tal_list[item+3]:
        increased+=1
        item+=1
    else:
        item+=1

print(increased)