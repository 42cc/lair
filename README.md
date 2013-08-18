lair
====

## init

Requirements: Python3 (or Pypy3), MongoDB, node.js (for JS tests), SASS

Required node.js packages: karma, jasmine-node

Put your Twitter API keys to ``settings_local.py``

## running

``make twitter_home`` starts daemon that connects to Twitter via streaming API and puts new tweets into database

``make run`` starts web server on port 8000

``make sass`` rebuilds CSS files from SASS (runs as a daemon)

## tests

``make test`` runs Python tests

``make test_js`` runs JavaScript tests
