# -*- coding: utf-8 -*-
#!/usr/bin/env python

from unittest import TestCase
from pymongo import MongoClient
from mock import patch

from .twitter_home import main
from lair.settings import MONGO_CONNECTION, MONGO_DB


def _mocked_reply():
    test_reply = [
        {"friends": []},
        {"id": 365205651267416064, "text": "test1"},
        {"id": 365205746851393536, "text": "test2"},
        {"id": 365215008914800640, "text": "test3"},
    ]
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
        tweet = db.twitter_home.find_one({"_id": 365205651267416064})
        self.assertEqual(tweet["text"], "test1")
