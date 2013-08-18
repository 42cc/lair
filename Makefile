sass:
	sass --watch -t expanded lair/web/static/sass:lair/web/static/css
test:
	TESTING=1 nosetests
test_js:
	karma start lair/web/js_tests/config/karma.conf.js
run:
	python -m lair.web.main --debug=1 --port=8000
twitter_home:
	python -m lair.backend.twitter_home
