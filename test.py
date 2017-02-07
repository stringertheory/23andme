from seqseek import Chromosome, BUILD37, BUILD38

import read

answer = 'ACCTGGTGAGGGGACATGGG'
result = Chromosome(17, assembly=BUILD38).sequence(141224, 141244)
assert result == answer, "doesn't match docs https://github.com/23andMe/seqseek"

