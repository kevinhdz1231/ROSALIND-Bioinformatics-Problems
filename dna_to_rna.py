# change dna sequence to rna sequence
with open('rosalind_rna.txt') as dna_seq:
    read_seq = dna_seq.read().rstrip()
    dna_seq.close()

with open('rosalind_rna_solution.txt', 'w') as rna_seq:
    rna_seq.write(read_seq.replace('T', 'U'))
    rna_seq.close()
    
