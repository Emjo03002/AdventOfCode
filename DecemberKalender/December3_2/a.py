with open("text.txt", "r") as f:
	dig = f.read().splitlines()

def most_common(li: list, idx: int, bo: bool):
	fi = [i[idx] for i in li]
	ta = str(int(bo))
	co = fi.count(ta)
	ha = len(fi) / 2 

	if (co >= ha if bo else co <= ha):
		out = ta
	else:
		out = str(1 - int(ta))

	# print("idx: {}, ta: {}, co: {}, ha: {}, out: {}".format(idx, ta, co, ha, out))
	return out

def loop(li: list, bo: bool):
	for idx in range(len(li[0])):
		m = most_common(li, idx, bo)

		# print("Before:", len(li))
		# print(li)
		j = 0

		while j < len(li):
			if li[j][idx] == m:
				j += 1
			else:
				li.pop(j)

		# print("After:", len(li))
		# print(li, "\n")

		if len(li) == 1: # 
			return li[0]

o2 = loop(dig.copy(), True)
oxygen = int(o2, 2)
print("Oxygen: {} {}".format(o2, oxygen))

co2 = loop(dig.copy(), False)
carbon = int(co2, 2)
print("Carbon: {} {}".format(co2, carbon))

print("\n")
print("Product: {}".format(oxygen * carbon))