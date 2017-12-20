seq = input('enter dna sequence:')
a_count = 0
t_count = 0
g_count = 0
c_count = 0
for base in seq:
    if base == "A":
        a_count += 1
    elif base == "T":
        t_count += 1
    elif base == "G":
        g_count += 1
    else:
        c_count += 1

print("adenosine =", a_count, "thymidine =", t_count, "guanine =", g_count,
      "cytidine =", c_count)
