.PHONY: index serve clean install update-requirements

index:
	python3 search-typeahead/indexer.py

serve: index
	python3 search-typeahead/server.py

clean:
	find . -name '*.pyc' -delete

install:
	../bin/pip install -Ur requirements.txt

update-requirements: install
	../bin/pip freeze > requirements.txt
