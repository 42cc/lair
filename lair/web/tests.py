from tornado.testing import AsyncHTTPTestCase

from .main import application, SITE_NAME


class HelloWorldTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return application

    def test_index(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertIn(SITE_NAME, response.body.decode('UTF-8'))
