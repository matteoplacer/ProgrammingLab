import unittest
from Lezione7 import CSVFile

class TestCSVFile(unittest.TestCase):

    def test_init(self):

        csv_file = CSVFile('shampoo_sales.csv')
        
        self.assertEqual(csv_file.name, 'shampo_sales.csv')