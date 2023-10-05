seq1 = "abcdefghijklmnop"
seq2 = "abcdefghiiklmnop"

zip_seqs = zip(seq1, seq2)
#print(list(zip_seqs))

enum_seqs = enumerate(zip_seqs)
#print(list(enum_seqs))

for i, (a, b) in enum_seqs:
    if a != b:
        print(f'index: {i}')