#!/usr/bin/env python
import os

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from jinja2 import Environment, FileSystemLoader


SITE_NAME = 'Lair'
ROOT = os.path.dirname(__file__)
TEMPLATE_ROOT = os.path.join(ROOT, 'templates')
STATIC_PATH = os.path.join(ROOT, 'static')

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=1, help="run in debug mode", type=int)


def render_template(template, **context):
    loader = FileSystemLoader(TEMPLATE_ROOT)
    env = Environment(loader=loader)
    template = env.get_template(template)
    context.update({
        'site_name': SITE_NAME,
        })
    return template.render(**context)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        content = render_template('index.html')
        self.write(content)


def main():
    parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], debug=options.debug, static_path=STATIC_PATH)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
