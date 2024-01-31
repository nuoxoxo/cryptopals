def decipher_against_symbol( x: int, xstr: str ) -> str:
    res = ''
    for i in range(0, len(xstr), 2):
        res += chr(int(xstr[i:i + 2], 16) ^ x)
    return res

def decipher_bruteforce( xstr: str):
    # try : ascii [32,126]
    for x in range(32, 127):
        test = decipher_against_symbol (x, xstr)
        print('/try', chr(x), '/str', test)
    print('/bruteforce ends\n')

HEX = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
decipher_bruteforce( HEX )

hidden = decipher_against_symbol(ord('X'), HEX)
print('/hidden -', hidden)
