import unittest
import convdolar

class MyTestCase(unittest.TestCase):
    def test_conversor(self):
        self.assertEqual(convdolar.conversor(20,3),60)

    def test_conversor2(self):
        self.assertEqual(convdolar.conversor(20,0),0)


if __name__ == '__main__':
    unittest.main()
