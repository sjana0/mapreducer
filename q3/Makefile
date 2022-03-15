all: say_hello generate
say_hello:
	@echo "Query 3"
generate:
	(cat resultq2.txt && cat network.txt)|python3 mapper.py|sort|python3 reducer.py > result.txt
clean:
	rm result.txt