import unittest
from calculator import*
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,2),5)
        self.assertEqual(add(3,6),9)
    def test_sub(self):
        self.assertEqual(sub(3,2),1)
        self.assertEqual(sub(3,6),-3)
    def test_multi(self):
        self.assertEqual(multi(3,2),6)
        self.assertEqual(multi(3,6),18)
    def test_div(self):
        self.assertEqual(div(3,2),1.5)
        self.assertEqual(div(3,6),0.5)
        self.assertEqual(div(1,0),"Error")
if __name__=='__main__':
    unittest.main()
    
