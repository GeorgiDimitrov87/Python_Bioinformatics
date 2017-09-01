from collections import Counter

f = open("dna.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ", "")
        f = f.replace("\n", "")
        seq = seq + f
    else:
        sequences.append(seq)
        seq = ""

# add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    length = len(sequence)
    repeats = []
    for i in range(length):
        repeats.append(sequence[i:i + 12])
    return repeats

all_repearts = []
for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        if len(j) == 12:
            all_repearts.append(j)

print(Counter(all_repearts))

def most_common(lst):
return max(set(lst), key=lst.count)

print(most_common(all_repearts))
print(all_repearts.count(most_common(all_repearts)))