import sys
def reducer():
	count = 0
	curr = ""
	t = ""
	for line in sys.stdin:
		curr = line.strip().split(" ")[0]
		if(t == ""):
			t = curr
			count = 1
		elif(t == curr):
			count += 1
		else:
			print(t, count)
			count = 1
			t = curr
	print(t, count)

reducer()