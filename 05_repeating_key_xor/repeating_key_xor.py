KEY = 'ICE'
TXT = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
REF = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

def rep_key_xor ( rep_key: str, plaintext: bytes ) -> bytes:
    index = 0
    res = ''
    for c in plaintext:
        """
        if c == '\n':
            res += '\n'
            continue"""
        key = rep_key [index]
        char = hex( ord(c) ^ ord(key) )[2:]
        if len(char) == 1:
            char = '0' + char
        res += char
        index = (index + 1) % 3
    return res

def hexify ( plaintext: bytes ) -> bytes:
    res = ''
    for c in plaintext:
        print(c, ord(c))
        res += str( hex(ord(c))[2:] )
    return res

res = rep_key_xor( KEY, TXT )
print('/res', repr(res))
print('/ref', repr(REF))

assert res == REF

