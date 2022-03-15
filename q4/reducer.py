import sys
def reducer():
	curr = ""
	count = 0
	maxid = ""
	max = 0
	for line in sys.stdin:
		a = line.strip().split(" ")
		if(curr == ""):
			curr = a[0]
			if(a[0] != a[1]):
				count += 1
				if(count > max):
					max = count
					maxid = curr
		elif(curr == a[0] and a[0] != a[1]):
			count += 1
			if(count > max):
				max = count
				maxid = curr
		elif(curr != a[0]):
			curr = a[0]
			if(a[0] != a[1]):
				count = 1
			else:
				count = 0
	print(maxid, max)

reducer()