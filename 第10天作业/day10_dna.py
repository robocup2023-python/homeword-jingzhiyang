codon_dict = {}
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

print(codon_dict)


def transcript(dna: str) -> str:
    dna = dna.rstrip("\n")
    return dna.replace("T", "U")


def translate(dna: str) -> str:
    # print(dna)
    rna = transcript(dna)
    res = ""
    start = rna.find("AUG")
    for i in range(start, len(rna), 3):
        if not rna[i:i + 3] in stops:
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
    print(transcript(value))
    protein_dict[key] = translate(value)
print(protein_dict)
