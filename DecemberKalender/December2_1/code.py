cords = open("text.txt", "r").read().splitlines()

fram = [st for st in cords if "forward" in st]
ner = [st for st in cords if "down" in st]
up = [st for st in cords if "up" in st]
x=y=z=0
svar=0


for s in fram:
    fval=s.strip("forward")
    i= int(fval)
    type(i)
    x += i
for s in ner:
    fval=s.strip("down")
    i= int(fval)
    type(i)
    y += i
for s in up:
    fval=s.strip("up")
    i= int(fval)
    type(i)
    z += i

svar=(y-z)*x

print(svar)


l= len(cords)


