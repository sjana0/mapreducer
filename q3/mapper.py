import sys
def mapper():
	c = 0
	top = []
	for line in sys.stdin:
		if(c != 10):
			c += 1
			top.append(line.strip())
		else:
			line = line.strip().split(" ")
			if(line[1] in top):
				print(line[1], 1)

mapper()