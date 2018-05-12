from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open('rosalind_revc.txt') as dna_seq:
    mySeq = Seq(dna_seq.read().rstrip('/n'), IUPAC.unambiguous_dna)
    dna_seq.close()

reverse_comp = mySeq.reverse_complement()

with open('rosalind_revc_solution.txt', 'w') as reverse_seq:
    reverse_seq.write(str(reverse_comp))
    reverse_seq.close()
    
    
