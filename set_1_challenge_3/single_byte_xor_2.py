from collections import defaultdict

def Print_dict (D):
    for k, v in dict(sorted(D.items())).items(): print(k, v)
    print('/print dict ends')

def Frequencyof_plaintext (plaintext: str):
    Freq = defaultdict(float)
    size = len( plaintext )
    for c in plaintext:
        if not c.isalpha(): continue
        # ascii in [32,127)
        asc = ord(c)
        if 31 < asc < 127 and c != '\n':
            Freq [c] += 1
    for k in Freq:
        Freq[k] = round( Freq[k] / size, 4 )
        # Freq[k] = Freq[k] / size
    return Freq


plaintext = open(0).read()
print('/len', len(plaintext))

F = Frequencyof_plaintext (plaintext)
Print_dict (F)


def decipher_against_symbol( x: int, xstr: str ) -> str:
    res = ''
    for i in range(0, len(xstr), 2):
        res += chr(int(xstr[i:i + 2], 16) ^ x)
    return res

def decipher_bruteforce( xstr: str):
    # try : ascii [32,126]
    T = defaultdict(lambda: float('inf'))
    for x in range(32, 127):
        f = {}
        for key in F:
            f[key] = F[key]
        if not chr(x).isalpha(): continue
        test = decipher_against_symbol (x, xstr)
        table = Frequencyof_plaintext(test)
        for key in table:
            table[key] = abs(f[key] - table[key])
        S = sum(table.values())
        T[chr(x)] = min( T[chr(x)], S )
    Print_dict(T)
    print( min(T.items(), key=lambda x: x[1])  )

HEX = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
decipher_bruteforce( HEX )

