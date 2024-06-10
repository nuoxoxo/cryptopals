import base64

xstr = \
'49276d206b696c6c696e6720796f757220627261\
696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

comp = \
'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEg\
cG9pc29ub3VzIG11c2hyb29t'

print('/len - hex string', len(xstr))
print('/len - to produce', len(comp))

def encode_base64 (s: str) -> str:

    # 1 - since s is a hex string, we traverse it 2 chars at a time

    ascii_string = ''
    for i in range(0, len(s), 2):
        num_hex = s[i:i + 2]
        num_dec = int(num_hex, 16)
        char = chr(num_dec)
        ascii_string += char
    print('/hidden text -', ascii_string)

    # 2 - encode the unicode string into byte string w/ ascii to encoding

    byte_string = ascii_string.encode('ascii')
    print('/byte string -', byte_string)

    # 3 - encode the byte string w/ base64 encoding

    base64_byte_string = base64.b64encode( byte_string )
    print('/base64 rep. -', base64_byte_string)

    # final - convert the base64-encoded byte string back to Unicode/ASCII

    res = base64_byte_string.decode('ascii')
    print('/base64 dec. -', base64_byte_string)
    return res

res = encode_base64( xstr )

print('/encoded -', res)
assert res == comp

