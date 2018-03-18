# output the reverse compliment of a dna strand to a file
with open('rosalind_revc.txt') as dna_seq:
    read_seq = dna_seq.read().rstrip('/n')
    dna_seq.close()


# when you need to replace two things it is convention to introduce a temporary element
reverse_seq = read_seq[::-1]
reverse_compliment = reverse_seq.replace('A', 'Z').replace('T', 'A').replace('Z', 'T').replace('C', 'Z').replace('G', 'C').replace('Z', 'G') 

with open('rosalind_revc_solution.txt', 'w') as reverse_seq:
    reverse_seq.write(reverse_compliment)
    reverse_seq.close()
    
    
print(reverse_compliment)
