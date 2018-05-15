'''
ID: RNA
Title: Transcribing RNA into DNA

'''

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open('rosalind_rna.txt') as dna_seq:
    seq_dna = Seq(dna_seq.read().rstrip(), IUPAC.unambiguous_dna)
    dna_seq.close()

with open('rosalind_rna_solution.txt', 'w') as rna_seq:
    seq_rna = seq_dna.transcribe()
    rna_seq.write(str(seq_rna))
    rna_seq.close()



