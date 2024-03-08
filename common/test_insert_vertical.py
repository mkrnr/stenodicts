import unittest
import insert_vertical

class TestInsertVertical(unittest.TestCase):

    def test_shift_down(self):
        key=["PH-RBG"]
        with self.assertRaises(KeyError): 
            insert_vertical.lookup(key)

    def test_shift_down_insert_key(self):
        key=["PH-RBG","R-T"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{#left}')

    def test_shift_down_insert_key_hash(self):
        key=["PH-RBG","R-T","H-RB"]
        with self.assertRaises(KeyError): 
            insert_vertical.lookup(key)

    def test_insert_hash_below(self):
        key=["PH-RBG","R-T","H-RB","R-S"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{^#}{#left}{#down}{^#}')

    def test_insert_two_hashes_below(self):
        key=["PH-RBG","R-T","H-RB","H-RB","R-S"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{^#}{^#}{#left}{#left}{#down}{^#}{^#}')

    def test_insert_two_hashes_two_rows_below(self):
        key=["PH-RBG","PH-RBG","R-T","H-RB","H-RB","R-S"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{^#}{^#}{#left}{#left}{#down}{^#}{^#}{#left}{#left}{#down}{^#}{^#}')

    def test_insert_two_hashes_repeated_three_times(self):
        key=["PWH-FP","PH-RBG","R-T","H-RB","H-RB","R-S"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, '{^#}{^#}{#left}{#left}{#down}{^#}{^#}{#left}{#left}{#down}{^#}{^#}{#left}{#left}{#down}{^#}{^#}')
    
    def test_count_rows_simple_cases(self):
        self.assertEqual(1,insert_vertical._count_rows(["PH-RBG","R-T","H-RB","R-S"]))
        self.assertEqual(3,insert_vertical._count_rows(["PH-RBG","PH-RBG","PH-RBG","R-T","H-RB","R-S"]))

    def test_count_rows_up_and_down_cases(self):
        self.assertEqual(0,insert_vertical._count_rows(["PH-RBG","PH-RBG","PH-RBG","PH-FPL","PH-FPL","PH-FPL","R-T","H-RB","R-S"]))
        self.assertEqual(1,insert_vertical._count_rows(["PH-RBG","PH-RBG","PH-RBG","PH-FPL","PH-FPL","R-T","H-RB","R-S"]))
        self.assertEqual(2,insert_vertical._count_rows(["PH-RBG","PH-RBG","PH-RBG","PH-FPL","R-T","H-RB","R-S"]))

    def test_get_strokes_to_insert(self):
        self.assertEqual(["H-RB"],insert_vertical._get_strokes_to_insert(["PH-RBG","R-T","H-RB","R-S"]))
        self.assertEqual(["H-RB","H-P"],insert_vertical._get_strokes_to_insert(["PH-RBG","R-T","H-RB","H-P","R-S"]))


if __name__ == '__main__':
    unittest.main()