def unhexify_xor ( key: int, hex_string: bytes ) -> bytes:
    res = ''
    for i in range(0, len( hex_string ), 2):
        res += chr(int(hex_string[i:i + 2], 16) ^ key)
    return res

"""
Get a model Score : from a piece of plaintext - eg. moby dick
"""

def get_freq(text: bytes) -> dict:
    from string import ascii_letters
    alpha_count = {}
    for c in ascii_letters:
        alpha_count [c] = text.count(c)
    size = len(text)
    freq = { c: round(alpha_count[c] / size, 8) for c in ascii_letters }
    return freq


def get_freq_alpha_only(text: bytes) -> dict:
    from string import ascii_letters
    alpha_count = {}
    for c in ascii_letters:
        alpha_count [c] = text.count(c)
    size_alpha = sum( alpha_count.values() )
    freq_alpha = { c: round(alpha_count[c] / size_alpha, 6) for c in ascii_letters }
    return freq_alpha


"""
Hex to plaintext string
"""

def get_score(text: bytes, model) -> float:
    res = 0.0
    size = len(text)
    for char, freq in model.items():
        res += abs( text.count(char) / size - freq)
    return res


def decipher_xored_hex_string (cipher: bytes, model) -> list:
    res = []
    for char in range(32, 127):
        #if not chr(char).isalpha(): ### MAJOR BUG FIX . XXX
            #continue
        test = unhexify_xor(char, cipher)
        score = get_score(test, model)
        res.append( (score, test) )
    return sorted(res)[0]


if __name__ == "__main__":
    text = open('mobydick.txt').read() # moby dick
    frequencies = get_freq_alpha_only (text)
    ciphers = open('4.in').read().splitlines()
    
    A = []
    for cipher in ciphers:
        temp = decipher_xored_hex_string(cipher, frequencies)
        A.append(temp)
    for a in sorted(A,reverse=True):print(a)
    print('/min:', min(A))

