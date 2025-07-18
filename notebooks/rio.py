#!/usr/bin/env python

def read_fasta(file):
    """
    Reads a fasta file and returns a dictionary with the name of the sequence as key and the
    nucleotide sequence as value.

    Parameters
    ----------
        file : str
            Path to the fasta file

    Returns
    -------
        fasta : dict
            Dictionary with the name of the sequence as key and the nucleotide sequence as value

    Examples
    --------
    >>> read_fasta("data/sequence.fasta")
    {'seq1': 'ACGTGAGCTAGC', 'seq2': 'ACGTGAGCTAGC'}
    """
    fasta = {}
    with open(file, "r") as f:
        data = f.read().split(">")
        for seq in data:
            name = seq.split("\n")[0]
            nuc = "".join(seq.split("\n")[1:])
            fasta[name] = nuc
    return fasta