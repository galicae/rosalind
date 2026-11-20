def reverse_complement(s):
    reverse = s[::-1]
    reverse = reverse.replace('A', 't')
    reverse = reverse.replace('T', 'a')
    reverse = reverse.replace('C', 'g')
    reverse = reverse.replace('G', 'c')
    return reverse.upper()