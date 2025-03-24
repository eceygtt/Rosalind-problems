DNASEQUENCES=['ATCGA','TTAGC','ACCTAG']
for sequence in DNASEQUENCES:
    reverse=reverse_sequence(sequence)
    reverse_complement=complement_sequence(reverse)
    print('sequence:          ',sequence)
    print('reverse:           ',reverse)
    print('reverse complement:',reverse_complement)