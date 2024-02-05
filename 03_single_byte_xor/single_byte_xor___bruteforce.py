def unhexify_xor ( key: int, hex_string: bytes ) -> bytes:
    res = ''
    for i in range(0, len( hex_string ), 2):
        res += chr(int(hex_string[i:i + 2], 16) ^ key)
    return res

def decipher_bruteforce( hex_cipher: bytes):
    # try : ascii [32,126]
    for candidate_char in range(32, 127):
        if not chr(candidate_char).isalpha():
            continue
        test_result = unhexify_xor( candidate_char, hex_cipher )
        print('/try', chr( candidate_char ), '/str', test_result)
    print('/bruteforce ends\n')

cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

if __name__ == "__main__":
    # brute force it
    decipher_bruteforce( cipher )

    # now that 'X' seems correct
    res = unhexify_xor( ord('X'), cipher )
    print('/hidden -', res)
