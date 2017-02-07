from seqseek import Chromosome, BUILD37

import read

reference = Chromosome(17, assembly=BUILD37)

for snp in read.genome():
    if snp.chromosome == 'X':
        print snp
    # print snp.genotype, reference.sequence(snp.position, snp.position + len(snp.genotype))
    
