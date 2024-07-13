.PHONY: run
run:
	python3 main.py

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf *.pyc

.PHONY: test
test:
	python3 test_main.py

.PHONY: check
check:
	pylint main.py
	pylint test_main.py
	mypy main.py
	mypy test_main.py
