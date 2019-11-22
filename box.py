import os
import sys
import argparse
import matplotlib.pyplot as plt
from matplotlib import rc


def initialize():
    """
    An argument parser as an initializing function
    """

    parser = argparse.ArgumentParser(
        description='This function plots the gene expression distribution \
                    across a set of genes for a set of tissue group, given \
                    the set of tissue groups, the set of genes, and the \
                    name of the output file.')
    parser.add_argument('-g',
                        '--gene',
                        nargs='+',
                        type=str,
                        help='The name of the target gene.',
                        required=True)
    parser.add_argument('-t',
                        '--tissue',
                        nargs='+',
                        type=str,
                        help='The name of the tissue group')
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help='The file name of the output file.',
                        required=True)

    args_parse = parser.parse_args()

    return args_parse


def boxplot(data, meta_file, y_label, title, output):
    plt.subplots(nrows=len(data), figsize=(10, 20))
    for i in range(len(data)):
        plt.subplot(len(data), 1, i + 1)
        plt.boxplot(data[i])
        plt.ylabel(y_label)
        plt.title(title[i])
        plt.xticks(range(1, len(meta_file) + 1), meta_file)

        if i == len(data) - 1:
            plt.xlabel('Gene')

    plt.savefig(output)


def main():
    args = initialize()

    rc('font', **{
        'family': 'sans-serif',
        'sans-serif': ['DejaVu Sans'],
        'size': 10
    })
    # Set the font used for MathJax - more on this later
    rc('mathtext', **{'default': 'regular'})
    plt.rc('font', family='serif')

    tissue_samples_txt, gene_counts_txt = [], []

    for i in range(len(args.tissue)):
        tissue_samples_txt.append('%s_samples.txt' % args.tissue[i])
        if not os.path.exists(tissue_samples_txt[i]):
            print('Input dataset (tissue_samples.txt) not found!')
            sys.exit(1)

    for i in range(len(args.gene)):
        gene_counts_txt.append('%s_counts.txt' % args.gene[i])
        if not os.path.exists(gene_counts_txt[i]):
            print('Input dataset (gene_counts.txt) not found!')
            sys.exit(1)

    sample_dist = {}   # (ID, tissue_group) pair
    gene_dist = {}     # (ID, counts) pair

    data_all = []
    for i in range(len(args.tissue)):
        tissue_id = []
        tissue_data = open(tissue_samples_txt[i])
        for l in tissue_data:
            tissue_id.append(l.split()[0])
            sample_dist[l.split()[0]] = args.tissue[i]

        counts_all = []
        for j in range(len(args.gene)):
            gene_id = []
            counts = []
            gene_data = open(gene_counts_txt[j])
            for l in gene_data:
                gene_id.append(l.split()[0])
                gene_dist[l.split()[0]] = int(l.split()[1])
            intersection_id = [id for id in tissue_id if id in gene_id]
            counts = [gene_dist[intersection_id[k]]
                      for k in range(len(intersection_id))]
            counts_all.append(counts)    # counts of each gene type
        data_all.append(counts_all)

    boxplot(data_all, args.gene, 'Count', args.tissue, args.output)


if __name__ == '__main__':
    main()
