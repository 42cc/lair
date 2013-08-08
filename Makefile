sass:
	sass --watch -t expanded lair/web/static/sass:lair/web/static/css
test:
	TESTING=1 nosetests
run:
	PYTHONPATH=$(CURDIR) ./lair/web/main.py --debug=1 --port=8000
twitter_home:
	PYTHONPATH=$(CURDIR) ./lair/backend/twitter_home.py
