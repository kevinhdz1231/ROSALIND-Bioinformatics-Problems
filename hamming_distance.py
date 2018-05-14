''' It is important to note that this program will only work if there
    is a single hamming distance '''

with open('rosalind_hamm.txt') as seqs:
    for line, sequence in enumerate(seqs):
        if line == 0:
            seq1 = str(sequence)
        if line == 1:
            seq2 = str(sequence)


hamm_distance = 0
for index, base in enumerate(seq1):
    if base != seq2[index]:
    
        hamm_distance += 1
    else:
        pass

print(hamm_distance)
