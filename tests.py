from tornado.testing import AsyncHttpTestCase


from .main import application, SITE_NAME


class HelloWorldTestCase(AsyncHttpTestCase):
    def get_app(self):
        return application

    def test_index(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertIn(SITE_NAME, response.body)
