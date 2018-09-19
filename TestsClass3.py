import unittest

class TestsClass3(unittest.TestCase):

    def setUp(self):
        print("this is in the setup method")
        pass

    def test_error(self):
        print("this should end as an error")
        raise("this is the exception message")
        pass

    def tearDown(self):
        print("this is in the tear down method")
        pass