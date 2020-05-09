.PHONY: test run_test main run_main clean

test: run_test clean

run_test:
	python3 -m search-typeahead.tests.test_indexing

main: run_main clean

run_main:
	python3 -m search-typeahead.src.main

clean:
	find . -name '*.pyc' -delete

help:
	@echo "   clean"
	@echo "     - removes all .pyc (pycache) files"
	@echo "   test"
	@echo "     - runs test files under search-typeahead/tests and clean"
	@echo "   run"
	@echo "     - runs main file under search-typeahead/src and clean"
	@echo ""