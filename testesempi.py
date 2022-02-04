import unittest
from esempi import somma

class TestSomma (unittest.TestCase):
    def test_somma (self):
        self.assertEqual(somma(1,3),4)
        self.assertEqual(somma(1.1,2.3),3.4)

#python -m unittest discover