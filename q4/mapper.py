import sys
def mapper():
	dept = []
	ids = []
	with open("dept_labels.txt", "r") as file:
		for line in file:
			a = line.strip().split(" ")
			ids.append(a[0])
			dept.append(a[1])
	with open("network.txt", "r") as file:
		for line in file:
			a = line.strip().split(" ")
			print(dept[ids.index(a[0])], dept[ids.index(a[1])])

mapper()
