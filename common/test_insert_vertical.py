import unittest
import insert_vertical

class TestInsertVertical(unittest.TestCase):

    def test_upper(self):
        key=["PH-RBG","-PBS","H-RB","R-R"]
        result=insert_vertical.lookup(key)
        self.assertEqual(result, 'FOO')


if __name__ == '__main__':
    unittest.main()