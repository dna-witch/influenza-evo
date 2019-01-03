### Translating cDNA to RNA to Protein ###
# input file should be a text file containing all of the "hmmemit" output seqs
# input file is cDNA from the RNA, so no Uracils, only Thymines

file_name = "gen_seq_set.txt"
cDNA = open(file_name, "rt").read() # need to turn the cDNA back into RNA so it can be translated

rna = cDNA.replace("T", "U")

print(rna) # just to check that everything is working

# create a dictionary with all the codons and their respective amino acid keys
codon_table = {

    'UUU': 'F',         'CUU': 'L',     'AUU': 'I',     'GUU': 'V',

    'UUC': 'F',         'CUC': 'L',     'AUC': 'I',     'GUC': 'V',

    'UUA': 'L',         'CUA': 'L',     'AUA': 'I',     'GUA': 'V',

    'UUG': 'L',         'CUG': 'L',     'AUG': 'M',     'GUG': 'V',

    'UCU': 'S',         'CCU': 'P',     'ACU': 'T',     'GCU': 'A',

    'UCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',

    'UCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',

    'UCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',

    'UAU': 'Y',         'CAU': 'H',     'AAU': 'N',     'GAU': 'D',

    'UAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',

    'UAA': 'STOP_CODON',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',

    'UAG': 'STOP_CODON',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',

    'UGU': 'C',         'CGU': 'R',     'AGU': 'S',     'GGU': 'G',

    'UGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',

    'UGA': 'STOP_CODON',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',

    'UGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'

}

def protein_seq(rna):
    seq = ''

    for i in range(0, len(rna), 3):
        aa = codon_table[rna[i:i+3]]
        if aa == 'STOP_CODON':
            break
        seq += aa

    print(seq)

prot = protein_seq(rna)

print(prot)
