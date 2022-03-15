import sys

def mapper():
    for line in sys.stdin:
        line = line.strip().split(" ")
        print(line[1], line[0])

mapper()