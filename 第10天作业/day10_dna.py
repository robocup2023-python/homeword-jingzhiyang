from collections import defaultdict
codon_dict = defaultdict(str)
stops = set()
with open("./asset/codon.txt") as codon:
    line = codon.readline()
    while line:
        code, protein = line.split()
        if len(code) == 3:
            codon_dict[code] = protein
            if protein == "stop":
                stops.add(code)
        line = codon.readline()

# print(codon_dict)
# print(stops)


def transcript(dna: str) -> str:
    res = ""
    projection = {"A": "U", "T": "A", "C": "G", "G": "C"}
    dna = dna.rstrip('\n')
    for t in dna:
        res += projection[t]
    return res



def translate(dna: str) -> str:
    # print(dna)
    rna = transcript(dna)
    res = ""
    start = rna.find("AUG")
    for i in range(start, len(rna), 3):
        if not rna[i:i + 3] in stops:
            # print(rna[i:i + 3])
            res += codon_dict[rna[i:i + 3]]
        else:
            break
    return res


seq_dict = {}
with open("./asset/seq.fa", "r") as seq:
    line = seq.readline()
    while line:
        if line.startswith(">"):
            seq_dict[line.lstrip(">").rstrip("\n")] = seq.readline()
        line = seq.readline()

protein_dict = {}
for key, value in seq_dict.items():
    # print(transcript(value))
    # print(translate(value))
    protein_dict[key] = translate(value)
print(protein_dict)


# GAGUUUUCAG AUG UCG GUG GCA GGU ACC UCG UCC AUC GAC GAC CCG AGG CCC CUG UGA AAC GCA AGC CCG ACC CUC GCA CGA AAG GUG CUG CCA CUG UGC GAA GGG ACC UAA CCG UCG GUC UGA CGG AAG GCC CAG UGA CGG UAC CUC CUC GGC GUC AGU CUA GGA UCG CAG CUC GGG GGA GAC UCA GUC CUU UGU AAA AGU CUG GAU AC
# CAAAAUG AGG UGG CAG GUG GUG UUG UUC GCU GCC CCU UUU ACA CCG CCG AAC UUC CCA CCA UCG CUA CAU UAC GCC CUA CCA GGG AGU GGU CCU UGG UCC CGG GCC UCA GCC UCG UCG GCG CUG CCG CCG CCG CAA CUC GUC CAG AAA CUA GGC CGG AGU ACU CUU GGC UUG GUA CCA CCU AUA GUA ACG GCU AGU GGG ACG UCU CAA UCA GGC UUG ACU GUC GGG G
# CAAAAUGAGGUGGCAGGUGGUGUUGUUCGCUGCCCCUUUUACACCGCCGAACUUCCCACCAUCGCUACAUUACGCCCUACCAGGGAGU GGU CCU UGG UCC CGG GCC UCA GCC UCG UCG GCG CUG CCG CCG CCG CAA CUC GUC CAG AAA CUA GGC CGG AGU ACU CUU GGC UUG GUA CCA CCU AUA GUA ACG GCU AGU GGG ACG UCU CAA UCA GGC UUG ACU GUC GGG G
"""
{'GCG': 'A', 'GCA': 'A', 'GCC': 'A', 'GCU': 'A', 'UGC': 'C', 'UGU': 'C', 'GAC': 'D', 'GAU': 'D', 'GAG': 'E', 'GAA': 'E',
 'UUC': 'F', 'UUU': 'F', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GGU': 'G', 'CAC': 'H', 'CAU': 'H', 'AUA': 'I', 'AUC': 'I',
 'AUU': 'I', 'AAG': 'K', 'AAA': 'K', 'UUG': 'L', 'UUA': 'L', 'CUG': 'L', 'CUA': 'L', 'CUC': 'L', 'CUU': 'L', 'AUG': 'M',
 'AAC': 'N', 'AAU': 'N', 'CCG': 'P', 'CCA': 'P', 'CCC': 'P', 'CCU': 'P', 'CAG': 'Q', 'CAA': 'Q', 'CGG': 'R', 'CGA': 'R',
 'CGC': 'R', 'CGU': 'R', 'AGG': 'R', 'AGA': 'R', 'UCG': 'S', 'UCA': 'S', 'UCC': 'S', 'UCU': 'S', 'AGC': 'S', 'AGU': 'S',
 'ACG': 'T', 'ACA': 'T', 'ACC': 'T', 'ACU': 'V', 'GUA': 'V', 'GUG': 'V', 'GUU': 'W', 'UGG': 'W', 'UAC': 'Y', 'UAU': 'Y',
 'GUC': 'V', 'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop'}
{'UAG', 'UGA', 'UAA'}
"""
#
#