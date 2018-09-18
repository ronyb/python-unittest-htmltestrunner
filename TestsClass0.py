import unittest

class TestsClass0(unittest.TestCase):

    def setUp(self):
        print("this is in the setup method")
        pass

    def test_pass(self):
        print("this should pass...")
        pass

    def test_fail(self):
        print("this should fail...")
        self.assertEqual(1, 0, "broken")
        pass

    def tearDown(self):
        print("this is in the tear down method")
        pass