import sys
sys.path.append("..")
from src.server.application import create_app
from src.routes.status import get_ip
import unittest
import json

class ServerSpec(unittest.TestCase):

    def setUp(self):
        config = {
            'TESTING': True,
        }
        self.app = create_app(config).test_client()

    def tearDown(self):
        pass

    def test_successful_status(self):
        expectedIp = get_ip()
        expectedData = {'status': 'OK', 'ip': '{}'.format(expectedIp)}
        response = self.app.get('/api/v1/status', follow_redirects=True)
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(json.loads(response.data), expectedData)


if __name__ == '__main__':
    unittest.main()