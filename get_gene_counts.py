import os
import sys
import gzip
import argparse

def initialize():
    """
    An argument parser as an initializing function
    """

    parser = argparse.ArgumentParser(
        description='This function takes a gene count file, a gene name, and \
                    an output file as parameters, and creates a file with the \
                    sample IDs and counts for that gene.')
    parser.add_argument('-i',
                        '--data',
                        type=str,
                        help='The file name of the dataset.',
                        required=True)
    parser.add_argument('-g',
                        '--gene',
                        type=str,
                        help='The name of the target gene.',
                        required=True)
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help='The file name of the output file.',
                        required=True)

    args_parse = parser.parse_args()

    return args_parse

def get_gene_data(data, gene, output):
    o = open(output, 'w')

    version = None
    dim = None
    header = None

    f = gzip.open(data, 'rt')
    for l in f:
        A = l.rstrip().split('\t')

        if version is None:
            version = A
            continue

        if dim is None:
            dim = A
            continue

        if header is None:
            header = A
            continue

        if A[1] == gene:
            for i in range(2, len(header)):
                o.write(header[i] + ' ' + A[i] + '\n')
                # For example, the first line should be
                # GTEX-1117F-0226-SM-5GZZ7 1993
    f.close()
    o.close()

def main():
    args = initialize()

    if not os.path.exists(args.data):
        print('Input dataset not found!')
        sys.exit(1)

    get_gene_data(args.data, args.gene, args.output)
    

if __name__ == '__main__':
    main()