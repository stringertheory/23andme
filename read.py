import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'Data')
GENOME_FILENAME = os.path.join(
    DATA_DIR,
    'genome_Michael_Stringer_v4_Full_20170206183314.txt',
)

def genome(filename=GENOME_FILENAME):
    with open(filename) as infile:
        for line in infile:
            if not line.startswith('#'):
                rsid, chromosome, position, genotype = line.strip().split('\t')
                yield rsid, int(chromosome), int(position), genotype

