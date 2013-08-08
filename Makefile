PYTHONPATH=`pwd`

sass:
	sass --watch -t expanded lair/web/static/sass:lair/web/static/css
test:
	TESTING=1 nosetests
run:
	./lair/web/main.py --debug=1 --port=8000
twitter_home:
	./lair/backend/twitter_home.py
