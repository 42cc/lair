#!/usr/bin/env python

import os

from twitter import TwitterStream, OAuth
from pymongo import MongoClient

from ..settings import TWITTER, MONGO_CONNECTION, MONGO_DB


def get_twitter_stream():
    stream = TwitterStream(
        domain="userstream.twitter.com",
        api_version="1.1",
        auth=OAuth(**TWITTER),
    )
    return stream.user()


def main():
    testing = os.environ.get('TESTING', '')
    mongo = MongoClient(**MONGO_CONNECTION)
    stream = get_twitter_stream()
    db = mongo[MONGO_DB]
    for tweet in stream:
        if "id" not in tweet:
            continue
        tweet["_id"] = tweet["id"]
        if not testing:
            print('({}) {}: {}'.format(
                tweet['id'], tweet["user"]["screen_name"], tweet["text"]))
        db.twitter_home.insert(tweet)


if __name__ == "__main__":
    main()
