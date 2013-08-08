# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from unittest import TestCase
import json
from pymongo import MongoClient
from mock import patch

from .twitter_home import main
from lair.settings import MONGO_CONNECTION, MONGO_DB


def _mocked_reply():
    path = os.path.dirname(__file__)
    test_reply = json.load(open(os.path.join(path, 'test_twitter.json')))
    for tweet in test_reply:
        yield tweet


class TwitterTestCase(TestCase):
    @patch('lair.backend.twitter_home.get_twitter_stream', _mocked_reply)
    def test_load_tweets(self):
        mongo = MongoClient(**MONGO_CONNECTION)
        db = mongo[MONGO_DB]
        db.drop_collection('twitter_home')
        main()
        self.assertEqual(db.twitter_home.count(), 3)
