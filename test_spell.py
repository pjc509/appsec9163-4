import unittest
import requests

server_address="http://127.0.0.1:5000"
server_login=server_address + "/login"

class FeatureTest(unittest.TestCase):
    def test_server_is_alive(self):
        req = requests.get(server_address)
        self.assertEqual(req.status_code, 200)

    def test_login_page_exists(self):
        req = requests.get(server_address + "/login")
        self.assertEqual(req.status_code, 200)

    #def test_page_exists(self):
    #    PAGES = ["", "/register", "/login"]
    #    for page in PAGES:
    #        req = requests.get(server_address + PAGES)
    #        self.assertEqual(req.status_code, 200)
   

if __name__ == '__main__':
        unittest.main()



