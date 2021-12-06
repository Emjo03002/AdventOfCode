cords = open("text.txt","r").read().splitlines()
cords = [s.split() for s in cords]
print(cords)
pos=0
depth=0
aim=0
for s in cords:
    if s[0] == "forward":
        pos += int(s[1])
        depth += aim*int(s[1])
    elif s[0] == "down":
        aim += int(s[1])
    elif s[0] == "up":
        aim -= int(s[1])
svar=depth*pos

print(svar)