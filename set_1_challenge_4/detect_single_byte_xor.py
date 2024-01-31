from collections import defaultdict

def Print_dict (D):
    for k, v in dict(sorted(D.items())).items(): print(k, v)
    print('/print dict ends')

def Frequencyof_plaintext (plaintext: str):
    Freq = defaultdict(float)
    size = len( plaintext )
    for c in plaintext:
        # ascii in [32,127)
        asc = ord(c)
        if 31 < asc < 127 and chr(_ord) != '\n':
            Freq [c] += 1
    for k in Freq:
        Freq[k] = round( Freq[k] / size, 4 )
        # Freq[k] = Freq[k] / size
    return Freq


plaintext = open(0).read()
print('/len', len(plaintext))

F = Frequencyof_plaintext (plaintext)
Print_dict (F)

infile = open('./4.in').read().strip()
#print(infile)

variance_chart = defaultdict(float)

for asc in range(32, 127):
    freq = defaultdict(int)
    for i in range(0, len(infile), 2):
        _ord = int(infile[i:i + 2], 16) ^ asc
        if 31 < _ord < 127 and chr(_ord) != '\n':
            freq[chr(_ord)] += 1
    for key in F:
        freq[key] -= F[key]
    variance_chart[chr(asc)] = sum(freq.values())

Print_dict(variance_chart)


