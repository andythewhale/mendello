"""
Andy Miller

This file is for storing basic building blocks.
You can pretty much import this file ever time, It shouldn't take up too much memory.
"""

#Defining Nucleic Acids & Stop Codon

#Positive:
Arg = 'Arg' #Arginine
His = 'His' #Histadine
Lys = 'Lys' #Lysine
Pos = [Arg, His, Lys] #Positive

#Negative:
Asp = 'Asp' #Aspartic Acid
Glu = 'Glu' #Glutamic Acid
Neg = [Asp, Glu] #Negative

#Polar Uncharged:
Ser = 'Ser' #Serine
Thr = 'Thr' #Threonine
Asn = 'Asn' #Asparagine
Gln = 'Gln' #Glutamine
Pun = [Ser, Thr, Asn, Gln] #Polar Uncharged

#Strange
Cys = 'Cys' #Cysteine
Sec = 'Sec' #Selenocysteine
Gly = 'Gly' #Glycine
Pro = 'Pro' #Proline
Str = [Cys, Sec, Gly, Pro] #Strange

#Hydrophobic
Ala = 'Ala' #Alanine
Val = 'Val' #Valine
Ile = 'Ile' #Isoleucine
Leu = 'Leu' #Leucine
Met = 'Met' #Methionine
Phe = 'Phe' #Phenylalanine
Tyr = 'Tyr' #Tyrosine
Trp = 'Trp' #Tryptophan
Hyd = [Ala, Val, Ile, Leu, Met, Phe, Tyr, Trp]

#Stop
Stop = 'Stop'

AA = Pos + Neg + Pun + Str + Hyd #Amino Acids