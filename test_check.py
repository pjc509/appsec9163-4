import unittest
import requests
from bs4 import BeautifulSoup

server_address="http://127.0.0.1:5000"
server_login=server_address + "/login"

def getElementbyID(text, id):
    soup=BeautifulSoup(text, "html.parser")
    result = soup.find(id="id")
    return result

def login(uname, pword, twofactor, session=None):
    addr = server_address + "/login"
    if session is None:
        session = requests.Session()
    #test_creds = {"username":uname, "password":pword, "twofa":twofactor}
    test_creds = {"uname":uname, "pword":pword, "twofa":twofactor}
    r = session.post(addr, data=test_creds)
    print("h1")
    print(r)
    print("h2")
    success = getElementbyID(r.text,"result")
    assert success != None, "Missing id='result' in your login response"
    return "success" in success.text


class FeatureTest(unittest.TestCase):
    #Unit test case 1
    def test_server_is_alive(self):
        req = requests.get(server_address)
        self.assertEqual(req.status_code, 200)

    #Unit test case 2
    def test_login_page_exists(self):
        req = requests.get(server_address + "/login")
        self.assertEqual(req.status_code, 200)

    #Unit test case 3
    def test_register_page_exists(self):
        req = requests.get(server_address + "/register")
        self.assertEqual(req.status_code, 200)

    #Unit test case 4
    def test_spell_page_exists(self):
        req = requests.get(server_address + "/spell_check")
        self.assertEqual(req.status_code, 200)

    def test_valid_login(self):
        login_addr = server_address + "/login"
        resp = login("crefeld", "crefeld", "1234567890")
        print("k1")
        print(resp)
        self.assertTrue(resp, "success! you are logged in")

    def test_invalid_login(self):
        login_addr = server_address + "/login"
        resp = login("crefeld", "crefeld1", "1234567890")
        self.assertFalse(resp, "login authentication is invalid")
   

if __name__ == '__main__':
        unittest.main()



