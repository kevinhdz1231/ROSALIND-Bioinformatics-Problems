'''
ID: PROT
Title: Translating RNA Into Protein
'''
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open('rosalind_prot.txt', 'r') as mySeq:
    rnaSeq = Seq((mySeq.read().replace('\n', "")), IUPAC.unambiguous_rna)
    mySeq.close()

proteinSeq = rnaSeq.translate()

with open('translate_rna_solution.txt', 'w') as protFile:
    stringSeq = str(proteinSeq)
    stringSeq = stringSeq.replace("*", "") # For some reason Biopython adds a "*" to the end of a translated protein sequence. This line fixes that.
    protFile.write(stringSeq)
    protFile.close()

