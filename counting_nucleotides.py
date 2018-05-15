'''
ID: DNA
Title: Counting DNA Nucleotides

'''

with open('rosalind_dna.txt') as seqfile:
    read_data = seqfile.read().rstrip()
    seq_dict = {"A":0,"C":0,"G":0,"T":0}
    for i in read_data:
        seq_dict[i] += 1

    for i in sorted(seq_dict.keys()):
        print (i, seq_dict[i])
