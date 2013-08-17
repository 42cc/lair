#!/usr/bin/env python
import os
import json

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from jinja2 import Environment, FileSystemLoader
import motor

from lair.settings import MONGO_CONNECTION, MONGO_DB


SITE_NAME = 'Lair'
ROOT = os.path.dirname(__file__)
TEMPLATE_ROOT = os.path.join(ROOT, 'templates')
STATIC_ROOT = os.path.join(ROOT, 'static')
STATIC_PATH = '/static/'

define("port", default=9001, help="run on the given port", type=int)
define("debug", default=0, help="run in debug mode", type=int)

mongo = motor.MotorClient(**MONGO_CONNECTION).open_sync()
db = mongo[MONGO_DB]


def render_template(template, **context):
    loader = FileSystemLoader(TEMPLATE_ROOT)
    env = Environment(loader=loader)
    template = env.get_template(template)
    context.update({
        'SITE_NAME': SITE_NAME,
        'STATIC_PATH': STATIC_PATH,
    })
    return template.render(**context)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        content = render_template('index.html', title="Buzz")
        self.write(content)


class TweetsHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        collection = self.get_argument('collection', 'twitter_home')
        last_id = self.get_argument('last_id', '')
        filters = {}
        if (last_id):
            filters['_id'] = {"$gt": int(last_id)}
        data = db[collection].find(filters).sort([('_id', -1)])
        if (not last_id):
            data = data.limit(20)
        data.to_list(100, self._got_data)

    def _got_data(self, data, error):
        if error:
            raise tornado.web.HTTPError(500, error)
        elif data:
            self.write(json.dumps(data))
        self.finish()


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/data/tweets/", TweetsHandler),
], debug=options.debug, static_path=STATIC_ROOT)


def main():
    parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
