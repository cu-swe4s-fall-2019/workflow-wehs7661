import unittest
import random
import os
import box


class TestBox(unittest.TestCase):
    def test_boxplot(self):
        data = [[[1, 2, 3, 4, 5]]]
        meta = ['A', 'B', 'C']
        title = 'test_boxplot'
        self.assertFalse(os.path.exists('test.png'))
        box.boxplot(data, meta, 'y-axis', 'test_boxplot', 'test.png')
        self.assertTrue(os.path.exists('test.png'))
        os.remove('test.png')


if __name__ == '__main__':
    unittest.main()
