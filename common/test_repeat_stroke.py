import unittest
import repeat_stroke

class TestInsertVertical(unittest.TestCase):
    def test_repeat_up_twice(self):
        key=["PWH-P","-FPL"]
        result=repeat_stroke.lookup(key)
        self.assertEqual(result, '{}{#up}{}{#up}')

    def test_repeat_up_eleven_times(self):
        key=["PWH-F","PWH-F","-FPL"]
        result=repeat_stroke.lookup(key)
        self.assertEqual(result, '{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}{}{#up}')

    def test_repeat_up_twice_two_times_in_a_row(self):
        key=["-FPL","PWH-P","-FPL"]
        result=repeat_stroke.lookup(key)
        self.assertEqual(result, '{}{#up}{}{#up}')

if __name__ == '__main__':
    unittest.main()