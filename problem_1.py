DNA="ATCTAGAGGATATAC"
def reverse_sequence(sequence):
    reverse=sequence[::-1]
    return reverse
reverse=reverse_sequence(DNA)
def complement_sequence(sequence):
    base_complements={'A':'T','T':'A','C':'G','G':'C'}
    complement_of_sequence=[base_complements[base] for base in sequence]
    complement_of_sequence=''.join(complement_of_sequence)
    return complement_of_sequence
reverse_complement=complement_sequence(reverse)
print('forward:',DNA)
print('reverse:',reverse) 
print(reverse_complement)
