# workflow-wehs7661
[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/workflow-wehs7661.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/workflow-wehs7661)

# Description
This is a repository for Assignment 10 of the course Software Engineering for 
Scientists (CSCI 7000) at CU Boulder, which includes the following files:
- `get_gene_counts.py`: A Python code for generating files like `SDHB_counts.txt`.
- `test_get_gene_counts.py`: Unit tests of `get_gene_counts.py`.
- `test_get_gene_counts.sh`: Functional tests of `get_gene_counts.py`.
- `get_tissue_samples.py`: A Python code for generating files like `Blood_samples.txt`
- `test_get_tissue_samples.py`: Unit tests of `get_tissue_samples.py`.
- `test_get_tissue_samples.sh`: Funtional tests of `get_tissue_samples.py`.
- `box.py`: A Python code for generating and saving a figure of boxplots.
- `test_box.py`: Unit tests of `box.py`.
- `test_box.sh`: Funtional tests of `box.py`.
- `GTEx_*`: two datasets used in this assignment
- `Snakefile`: A file which establishes a workflow of execution of the Python codes above.

# Installation
All the Python scripts are written in Python 3 and the packages required to run the codes include: `argparse`, `sys`, `matplotlib`, `os`, and `unittest`.

# Usage
To generate a box plot, simply run `snakemake`.

# Changes made upon the starter of Assignment 10
- Developed `get_gene_counts.py`, `get_tissue_samples.py` and `box.py`, which were requied in the workflow, and their corresponding unit tests and functional tests.
- Added `Snakefile` to enable the workflow.
- Make sure that all the Python codes conform with PEP8 coding style.
- Modified `.travis.yml` to pass TravisCI.
- Updated README.