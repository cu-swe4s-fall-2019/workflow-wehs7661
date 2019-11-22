import os
import sys
import argparse

def initialize():
    """
    An argument parser as an initializing function
    """

    parser = argparse.ArgumentParser(
        description='This function takes a sample attributes file, a tissue \
                    group (SMTS), and output file as parameters, and creates \
                    a file with all of the samples IDs (SAMPID) for that \
                    tissue group.')
    parser.add_argument('-i',
                        '--data',
                        type=str,
                        help='The file name of the sample attribute file.',
                        required=True)
    parser.add_argument('-t',
                        '--tissue',
                        type=str,
                        help='The name of the target tissue group',
                        required=True)
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help='The file name of the output file.',
                        required=True)

    args_parse = parser.parse_args()

    return args_parse


def get_tissue_data(data, tissue, output):
    o = open(output, 'w')

    header = None
    sampid_col = -1
    smts_col = -1

    f = open(data)
    for l in f:
        A = l.rstrip().split('\t')
        if header is None:
            header = A
            sampid_col = A.index('SAMPID')  # sampid_col = 0
            smts_col = A.index('SMTS')      # smts_col = some index ...
            continue

        if A[smts_col] == tissue:
            o.write(A[sampid_col] + '\n')
    f.close()
    o.close()

def main():
    args = initialize()

    if not os.path.exists(args.data):
        print('Input dataset not found!')

    get_tissue_data(args.data, args.tissue, args.output)

if __name__ == '__main__':
    main()