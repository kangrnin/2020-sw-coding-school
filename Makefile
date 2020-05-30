.PHONY: serve clean prefix

serve:
	export FLASK_APP=search-typeahead.app; flask run

clean:
	find . -name '*.pyc' -delete

prefix:
	export FLASK_APP=search-typeahead.app; flask make-prefix