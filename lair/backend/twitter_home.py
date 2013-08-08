#!/usr/bin/env python

from twitter import TwitterStream, OAuth
from pymongo import MongoClient


from lair.settings import TWITTER, MONGO_CONNECTION, MONGO_DB


def get_twitter_stream():
    stream = TwitterStream(
        domain="userstream.twitter.com",
        api_version="1.1",
        auth=OAuth(**TWITTER),
    )
    return stream.user()


def main():
    mongo = MongoClient(**MONGO_CONNECTION)
    stream = get_twitter_stream()
    db = mongo[MONGO_DB]
    next(stream)
    for tweet in stream:
        db.twitter_home.insert(tweet)


if __name__ == "__main__":
    main()
