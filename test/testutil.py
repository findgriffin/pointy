import unittest
from pointy import utils

class TestUtils(unittest.TestCase):
    def test_parse_date(self):
        pd = utils.parse_date
        self.assertEqual(pd('13/08/12'), '13/08/2012')
        self.assertEqual(pd('04/08/12'), '04/08/2012')
        self.assertEqual(pd('04/8/12'), '04/08/2012')
        self.assertEqual(pd('4 jul 13'), '04/07/2013')
        with self.assertRaises(ValueError):
            pd('')
        with self.assertRaises(ValueError):
            pd('foobar')

    def test_is_point_value(self):
        ipv = utils.is_point_value
        self.assertTrue(ipv('3'))
        self.assertTrue(ipv('-3'))
        self.assertTrue(ipv('0'))
        self.assertTrue(ipv('-0'))
        self.assertTrue(ipv('13412341234'))
        self.assertFalse(ipv('3.0'))
        self.assertFalse(ipv('-3.0'))
        self.assertFalse(ipv('-0f'))
        self.assertFalse(ipv('foo'))

    def test_process_item(self):
        pi = utils.process_item
        items = {'foo': 3, 'bar': -1}
        self.assertEqual(pi('foo', items), 
                ('foo', 3, 'used previous points 3 for foo'))
        self.assertEqual(pi('foo -4', items), 
                ('foo', -4, 'foo updated with points value -4'))
        self.assertEqual(pi('bar -1', items), 
                ('bar', -1, 'bar updated with points value -1'))
        self.assertEqual(pi('foo', items), 
                ('foo', -4, 'used previous points -4 for foo'))
        with self.assertRaises(ValueError):
            pi('', items)
        with self.assertRaises(ValueError):
            pi('baz', items)
        self.assertEqual(pi('baz 7', items), 
                ('baz', 7, 'baz updated with points value 7'))
        self.assertEqual(pi('baz', items), 
                ('baz', 7, 'used previous points 7 for baz'))
