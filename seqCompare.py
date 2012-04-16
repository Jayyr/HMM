import sys, math


"""
Takes in a fastaFile that contains two sequences and outputs a list of
comparison values at each position.
If different: output "D"
If identital: output "I"
"""
def compareSequences(fastaFile):
    fFile = open(fastaFile)
    seq1 = ""
    seq2 = ""
    seqID = 1
    if fFile.readline() == ">Sequence 1\n":
        seqID = 1
    for line in fFile:
        if line == ">Sequence 1\n":
            seqID = 1
            continue
        elif line == ">Sequence 2\n":
            seqID = 2
            continue
        if seqID == 1:
            seq1 += line.strip()
        elif seqID == 2:
            seq2 += line.strip()
    seqCompare = []
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            seqCompare.append('I')
        else:
            seqCompare.append('D')
    fFile.close()
    return seqCompare
    
