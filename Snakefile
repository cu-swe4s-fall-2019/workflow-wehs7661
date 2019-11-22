GENES = ["SDHB", "MEN1", "KCNH2", "MSH2", "MYL2", "BRCA2"]
TISSUES = ["Brain", "Heart", "Blood", "Skin"]

rule all:
    input:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'

rule gene_counts:
    input:
        'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
    output:
        expand('{gene}_counts.txt', gene=GENES)
    shell:
        'for gene in {GENES}; do ' \
        + 'python get_gene_counts.py -o $gene\_counts.txt -g $gene -i {input}; ' \
        + 'done'

rule tissue_samples:
    input:
        'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output:
        expand('{tissue}_samples.txt', tissue=TISSUES)
    shell:
        'for tissue in {TISSUES}; do ' \
        + 'python get_tissue_samples.py -o $tissue\_samples.txt -t $tissue -i {input}; ' \
        + 'done'


rule boxplot:
    input:
        rules.gene_counts.output,
        rules.tissue_samples.output
        
    output:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'
    shell:
        'python box.py -o {output} -g {GENES} -t {TISSUES} '