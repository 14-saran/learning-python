# test file setup
import unittest
import My_class

class TestClass(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(My_class.pluss(2,3),5)
        self.assertEqual(My_class.pluss(0,0),0)
        self.assertEqual(My_class.pluss(-2,3),0)


if __name__ == "__main__":
    unittest.main()