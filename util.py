"""
This is a python file that will contain the utility files that model certain events.
It will make things easier or it will do stuff that just seems to need to be taken
care of in a file that isn't a main file.

What should be included?
1. Transcription
2. Translation 
3.

"""


def translation(base_1, base_2, base_3):
    """
    -This function literally just takes in 3 mRNA base pairs and outputs what Amino Acid it codes for.
    -You'll need the buildingBlocks.py file imported to run this

    Takes in 3 bases as inputs

    Returns amino group
    """
    # Phe
    if base_1 == mrU and base_2 == mrU and base_3 == mrU or base_3 == mrC:
        amino = Phe

    # Leu
    if (base_1 == mrC or base_1 == mrU) and base_2 == mrU and (
                    base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Leu

    # Ile
    if base_1 == mrA and base_2 == mrU and (base_3 == mrU or base_3 == mrC or base_3 == mrA):
        amino = Ile

    # Met
    # Met is also the start codon
    if base_1 == mrA and base_2 == mrU and base_3 == mrG:
        amino = Met

    # Val
    if base_1 == mrG and base_2 == mrU and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Val

    # Ser
    if base_1 == mrU and base_2 == mrC and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Ser

    # Pro
    if base_1 == mrC and base_2 == mrC and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Pro

    # Thr
    if base_1 == mrA and base_2 == mrC and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Thr

    # Ala
    if base_1 == mrG and base_2 == mrC and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Ala

    # Tyr
    if base_1 == mrU and base_2 == mrA and (base_3 == mrU or base_3 == mrC):
        amino = Tyr

    # Stop
    if base_1 == mrU and (base_2 == mrA or base_2 == mrG) and (base_3 == mrA or base_3 == mrG):
        amino = Stop

    # His
    if base_1 == mrC and base_2 == mrA and (base_3 == mrU or base_3 == mrC):
        amino = His

    # Gln
    if base_1 == mrC and base_2 == mrA and (base_3 == mrA or base_3 == mrG):
        amino = Gln

    # Asn
    if base_1 == mrA and base_2 == mrA and (base_3 == mrU or base_3 == mrC):
        amino = Asn

    # Lys
    if base_1 == mrA and base_2 == mrA and (base_3 == mrA or base_3 == mrG):
        amino = Lys

    # Asp
    if base_1 == mrG and base_2 == mrA and (base_3 == mrU or base_3 == mrC):
        amino = Asp

    # Glu
    if base_1 == mrG and base_2 == mrA and (base_3 == mrA or base_3 == mrG):
        amino = Glu

    # Cys
    if base_1 == mrU and base_2 == mrG and (base_3 == mrU or base_3 == mrC):
        amino = Cys

    # Trp
    if base_1 == mrU and base_2 == mrG and base_3 == mrG:
        amino = Trp

    # Arg
    if base_1 == mrC and base_2 == mrG and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Arg

    # Ser
    if base_1 == mrA and base_2 == mrG and (base_3 == mrA or base_3 == mrG):
        amino = Ser

    # Arg
    if base_1 == mrA and base_2 == mrG and (base_3 == mrA or base_3 == mrG):
        amino = Arg

    # Gly
    if base_1 == mrG and base_2 == mrG and (base_3 == mrU or base_3 == mrC or base_3 == mrA or base_3 == mrG):
        amino = Gly

    # return amino group
    return amino