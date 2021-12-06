bi=open("text.txt", "r").read().splitlines()
tal = 0
bicopy = bi.copy()
print(bi == bicopy)
# För varje bit
    # Konstatera vilken som ska bort (0 eller 1)

    # Ta bort de som ska bort från bi

    # Tills det bara är en kvar 


for i in range(12):
    b = [it[i] for it in bi]

    tal = b.count("1")
    if tal >= (len(b)/2):
        bort = "0"
    else:
        bort= "1"

    j = 0
    print(bi)
    while j < len(bi):
        if bi[j][i] == bort:
            bi.pop(j)
        else:
            j += 1
        #print(len(bi))

    if len(bi) == 1:
        o2 = bi[0]
        break
print(bi)
#print(o2)

for i in range(12):
    b = [it[i] for it in bicopy]

    tal = b.count("0")
    #print(tal)
    if tal > (len(b)/2):
        bort = "0"
    else:
        bort = "1"
    print(bicopy)
    j = 0
    while j < len(bicopy):
        if bicopy[j][i] == bort:
            bicopy.pop(j)
        else:
            j += 1

        

    if len(bicopy) == 1:
        co2 = bicopy[0]
        break
print(bicopy)
print(co2, o2)
co2 = int(co2, base=2)
o2 = int(o2, base=2)
svar=o2*co2
print(svar)
    











# for s in b:
#     if tal[i] > (len(b)/2):
#         print(len(b))
#         if s !="1":
#             b.remove(s)
#             print(len(b))
#     if tal[i] < (len(b)/2):
#         if s !="0":
#             b.remove(s)
#             print(len(b))


    




            


 
        
            

# while len(bi)<0:
#     if tal[i] > 500:
#         tal[i]=1
#         tal
#     i+=1


