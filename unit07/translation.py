with open("codon_table.txt", "r") as file:
    codon_table = {}
    for line in file:
        line_info = line.strip().split(" ")
        codon = line_info[0]
        amino = line_info[1]
        codon_table[codon] = amino

with open("rna.txt", "r") as file:
    rna = file.readline().strip()

protein = ""
for i in range(0, len(rna), 3):
    codon = rna[i: i+3]
    if codon_table[codon] == "Stop":
        break
    else:
        protein += codon_table[codon]

print(protein)
print(len(protein))