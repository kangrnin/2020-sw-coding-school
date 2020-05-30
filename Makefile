.PHONY: serve clean prefix

serve:
	export FLASK_APP=search-typeahead.app; python3 -m search-typeahead.app

clean:
	find . -name '*.pyc' -delete

prefix:
	export FLASK_APP=search-typeahead.app; flask build-prefix