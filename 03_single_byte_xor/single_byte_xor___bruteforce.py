def unhexify_xor_by_key ( key: int, hex_string: bytes ) -> bytes:
    res = ''
    for i in range(0, len( hex_string ), 2):
        hex_value = int(hex_string[i:i + 2], 16)
        xor_value = hex_value ^ key
        char = chr(xor_value)
        res += char
    return res

def decipher_bruteforce( hex_cipher: bytes):
    # trying all ascii chars in range [32,126]
    for n in range(32, 127):
        if chr(n).isalpha():
            res = unhexify_xor_by_key (n, hex_cipher)
            print('/try', chr(n), '- /str', res)
    print('/bruteforce ends \n')

cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# 'X' seems correct verified using our eyes
decipher_bruteforce( cipher )
res = unhexify_xor_by_key( ord('X'), cipher )

print('/hidden -', res)

assert 'bacon' == res.split()[-1]

