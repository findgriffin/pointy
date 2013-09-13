import unittest
from pointy import utils

class TestUtils(unittest.TestCase):
    def test_parse_date(self):
        pd = utils.parse_date
        self.assertEqual(pd('13/08/12'), '13/08/2012')
        self.assertEqual(pd('04/08/12'), '04/08/2012')
        self.assertEqual(pd('04/8/12'), '04/08/2012')
        self.assertEqual(pd('4 jul 13'), '04/07/2012')
        with self.assertRaises(ValueError):
            pd('')
        with self.assertRaises(ValueError):
            pd('foobar')
