import sys

def mapper():
    for line in sys.stdin:
        print(line.strip().split(" ")[0], 1)

mapper()
