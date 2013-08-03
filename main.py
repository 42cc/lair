#!/usr/bin/env python
import os

import tornado.ioloop
import tornado.web
from jinja2 import Environment, FileSystemLoader


ROOT = os.path.dirname(__file__)
TEMPLATE_ROOT = os.path.join(ROOT, 'templates')


def render_template(template, **context):
    loader = FileSystemLoader(TEMPLATE_ROOT)
    env = Environment(loader=loader)
    template = env.get_template(template)
    return template.render(**context)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        content = render_template('index.html')
        self.write(content)


application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
