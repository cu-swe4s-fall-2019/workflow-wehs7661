#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_get_tissue_samples.py
assert_no_stdout
run test_style pycodestyle get_tissue_samples.py
assert_no_stdout

run test_Blood python get_tissue_samples.py -o test.txt -t Blood -i GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
assert_exit_code 0
assert_no_stdout
rm test.txt