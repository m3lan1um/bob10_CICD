import unittest
import hello

class TestHello(unittest.TestCase):
    def test_add(self):
        h = hello.Hello()
        result = h.add(2, 3)
        self.assertEqual(result, 5)
        result = h.add(2, 5)
        self.assertEqual(result, 7)
        
if __name__ == "__main__": 
    unittest.main()