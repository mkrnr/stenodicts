import unittest
import insert_vertical

class TestInsertVertical(unittest.TestCase):

    def test_shift_down(self):
        key=["PH-RBG"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{#shift(down)}')
    def test_shift_down_insert_key(self):
        key=["PH-RBG","R-T"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{#left}')

    # we only want to allow and record a limited list of inserted keys so we don't just throw a KeyError here
    def test_shift_down_insert_key_hash(self):
        key=["PH-RBG","R-T","H-RB"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{^#}')

    def test_insert_two_hash(self):
        key=["PH-RBG","R-T","H-RB","R-R"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{^#}{#left}{#down}{^#}')


if __name__ == '__main__':
    unittest.main()