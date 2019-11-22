#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle test_box.py
assert_no_stdout
run test_style pycodestyle box.py
assert_no_stdout

run test_no_file python box.py -t Brain -g SDHB -o test_file
assert_exit_code 1
assert_stdout