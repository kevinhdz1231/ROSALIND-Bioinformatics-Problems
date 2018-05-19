'''
ID: PERM
Title: Enumerating Gene Orders
'''
import itertools
import math

with open('rosalind_perm.txt') as num_file:
    num = int(num_file.read())
    num_file.close()

perm_nums = str()

for i in range(1, num + 1):
    perm_nums += str(i)

permutations = list(map(" ".join, itertools.permutations(perm_nums))) # creates a list containing each permutation
n_factorial = math.factorial(num)

with open('rosalind_perm_solutions.txt', 'w') as perm_file:
    perm_file.write("{}\n".format(str(n_factorial)))
    for i in permutations:
        perm_file.write("{}\n".format(i))
    perm_file.close()


    
    
