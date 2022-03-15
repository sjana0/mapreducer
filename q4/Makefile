all: say_hello generate
say_hello:
	@echo "Query 4"
generate:
	python3 mapper.py|sort|python3 reducer.py > result.txt
clean:
	rm result.txt