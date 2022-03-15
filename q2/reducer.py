import sys

def reducer():
    count = 0
    for line in sys.stdin:
        line = line.strip().split(" ")
        print(line[1])
        count += 1
        if(count == 10):
            break

reducer()