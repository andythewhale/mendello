"""
Andy Miller

This file is for storing basic building blocks.
You can pretty much import this file ever time, It shouldn't take up too much memory.
"""

# Defining DNA:
drA = 'drA'  # Adenine
drT = 'drT'  # Thymine
drC = 'drC'  # Cytosine
drG = 'drG'  # Guanine
DNA = [drA, drT, drC, drG]  # DNA

# Defining mRNA:
mrA = 'mrA'  # Adenine
mrU = 'mrU'  # Uracil
mrC = 'mrC'  # Cytosine
mrG = 'mrG'  # Guanine
mRNA = [mrA, mrU, mrC, mrG]  # mRNA

# Defining tRNA:
trA = 'trA'  # Adenine
trU = 'trU'  # Uracil
trC = 'trC'  # Cytosine
trG = 'trG'  # Guanine
tRNA = [trA, trU, trC, trG]  # tRNA

# Defining Nucleic Acids:

# Positive:
Arg = 'Arg'  # Arginine
His = 'His'  # Histadine
Lys = 'Lys'  # Lysine
Pos = [Arg, His, Lys]  # Positive

# Negative:
Asp = 'Asp'  # Aspartic Acid
Glu = 'Glu'  # Glutamic Acid
Neg = [Asp, Glu]  # Negative

# Polar Uncharged:
Ser = 'Ser'  # Serine
Thr = 'Thr'  # Threonine
Asn = 'Asn'  # Asparagine
Gln = 'Gln'  # Glutamine
Pun = [Ser, Thr, Asn, Gln]  # Polar Uncharged

# Strange
Cys = 'Cys'  # Cysteine
Sec = 'Sec'  # Selenocysteine
Gly = 'Gly'  # Glycine
Pro = 'Pro'  # Proline
Str = [Cys, Sec, Gly, Pro]  # Strange

# Hydrophobic
Ala = 'Ala'  # Alanine
Val = 'Val'  # Valine
Ile = 'Ile'  # Isoleucine
Leu = 'Leu'  # Leucine
Met = 'Met'  # Methionine
Phe = 'Phe'  # Phenylalanine
Tyr = 'Tyr'  # Tyrosine
Trp = 'Trp'  # Tryptophan
Hyd = [Ala, Val, Ile, Leu, Met, Phe, Tyr, Trp]

AA = Pos + Neg + Pun + Str + Hyd  # Amino Acids