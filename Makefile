sass:
	sass --watch -t expanded lair/web/static/sass:lair/web/static/css
run:
	./lair/web/main.py --debug=1 --port=8000
test:
	nosetests
