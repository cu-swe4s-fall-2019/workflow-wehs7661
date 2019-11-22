import unittest
import random
import os
import get_tissue_samples

class TestGetTissueSamples(unittest.TestCase):
    def test_get_tissue_data(self):
        tissue = 'Blood'
        data = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
        output = 'test.txt'
        self.assertFalse(os.path.exists('test.txt'))
        get_tissue_samples.get_tissue_data(data, tissue, output)
        self.assertTrue(os.path.exists('test.txt'))
        os.remove('test.txt')

if __name__ == '__main__':
    unittest.main()