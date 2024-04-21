from single_byte_xor___bruteforce import unhexify_xor_by_key
from string import ascii_letters

def printer_dict (D):
    print()
    for k, v in D.items(): print(k, v)
    print('/print dict ends')

def printer_dict_sorted (D):
    print()
    for k, v in dict(sorted(D.items())).items(): print(k, v)
    print('/print dict ends')


"""
Get a model Score from a piece of plaintext : eg. moby dick
"""
def frequency(text: bytes) -> dict:
    alpha_count = {}
    for c in ascii_letters:
        alpha_count [c] = text.count(c)
    # printer_dict (alpha_count)
    size = len(text)
    freq = { c: round(alpha_count[c] / size, 8) for c in ascii_letters }
    printer_dict( freq )
    return freq


def frequency_alpha_only(text: bytes) -> dict:
    alpha_count = {}
    for c in ascii_letters:
        alpha_count [c] = text.count(c)
    size_alpha = sum( alpha_count.values() )
    freq_alpha = { c: round(alpha_count[c] / size_alpha, 6) for c in ascii_letters }
    # printer_dict( freq_alpha )
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
        if chr(char).isalpha():
            test = unhexify_xor_by_key (char, cipher)
            score = get_score(test, model)
            res.append( (score, test) )
    return sorted(res)[:5]


"""
Drive
"""
text = open('mobydick.txt').read()
frequencies = frequency_alpha_only (text)
cipher = open('3.in').read().strip()
res = decipher_xored_hex_string(cipher, frequencies)

for i, tup in enumerate(res):
    print(str(i) + '/', tup)

print('\n/res', res[0])

