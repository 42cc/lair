import json

from pymongo import MongoClient
from tornado.testing import AsyncHTTPTestCase

from .main import application, SITE_NAME
from lair.settings import MONGO_CONNECTION, MONGO_DB


class HelloWorldTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return application

    def test_index(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertIn(SITE_NAME, response.body.decode('UTF-8'))


class TweetsTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return application

    def test_tweets_default(self):
        mongo = MongoClient(**MONGO_CONNECTION)
        db = mongo[MONGO_DB]
        db.drop_collection('twitter_home')
        test_tweets = [
            {"_id": 365205651267416064, "text": "test1"},
            {"_id": 365205746851393536, "text": "test2"},
            {"_id": 365215008914800640, "text": "test3"},
        ]
        db.twitter_home.insert(test_tweets)

        self.http_client.fetch(self.get_url('/data/tweets/'), self.stop)
        response = self.wait()
        body = response.body.decode('UTF-8')
        obj = json.loads(body)

        self.assertEqual(len(obj), 3)
        self.assertEqual(obj[0]['_id'], 365215008914800640)
        self.assertEqual(obj[0]['text'], "test3")

    def test_tweets_by_last_id(self):
        mongo = MongoClient(**MONGO_CONNECTION)
        db = mongo[MONGO_DB]
        db.drop_collection('twitter_home')
        test_tweets = [
            {"_id": 365205651267416064, "text": "test1"},
            {"_id": 365205746851393536, "text": "test2"},
            {"_id": 365215008914800640, "text": "test3"},
        ]
        db.twitter_home.insert(test_tweets)

        self.http_client.fetch(self.get_url('/data/tweets/?last_id=365205651267416064'), self.stop)
        response = self.wait()
        body = response.body.decode('UTF-8')
        obj = json.loads(body)

        self.assertEqual(len(obj), 2)
        self.assertEqual(obj[0]['_id'], 365215008914800640)
        self.assertEqual(obj[0]['text'], "test3")
