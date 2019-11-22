import unittest
import random
import os
import get_gene_counts

class TestGetGeneCounts(unittest.TestCase):
    def test_get_gene_data(self):
        gene = 'SDHB'
        data = 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_' \
                +'reads.acmg_59.gct.gz'
        output = 'test.txt'
        self.assertFalse(os.path.exists('test.txt'))
        get_gene_counts.get_gene_data(data, gene, output)
        self.assertTrue(os.path.exists('test.txt'))
        os.remove('test.txt')

if __name__ == '__main__':
    unittest.main()
