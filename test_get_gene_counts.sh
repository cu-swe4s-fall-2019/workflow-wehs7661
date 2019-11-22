#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_get_gene_counts.py
assert_no_stdout
run test_style pycodestyle get_gene_counts.py
assert_no_stdout

run test_SDHB python get_gene_counts.py -o test.txt -g SDHB -i GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
assert_exit_code 0
assert_no_stdout
rm test.txt