all: say_hello generate
say_hello:
	@echo "Query 1"
generate:
	cat resultq1.txt|python3 mapper.py|sort -nr|python3 reducer.py > result.txt
clean:
	rm result.txt