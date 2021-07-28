import os
from database import Database
from flask.helpers import url_for
from server import app
import unittest

class Flasktest(unittest.TestCase):
    def test_index(self):
        tester =  app.test_client(self)
        response= tester.get("/")
        statuscode=response.status_code
        self.assertEqual(statuscode,200)
    def test_conent(self):
        tester =  app.test_client(self)
        response= tester.get("/")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")
    def test_create_data(self):
        tester =  app.test_client(self)
        response= tester.post("/",data={"message":"edwin"})
        self.assertEqual(response.status_code,200)

    if __name__=="__main__":
        unittest.main()