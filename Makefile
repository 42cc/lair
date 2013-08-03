sass:
	sass --watch -t expanded static/sass:static/css
run:
	./main.py --debug=1 --port=8000
test:
	nosetests tests.py
