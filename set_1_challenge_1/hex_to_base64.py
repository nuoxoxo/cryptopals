
xstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
comp = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def encode_base64 (s: str) -> str:
    import base64
    ascii_string = ''
    for i in range(0, len(s), 2):
        ascii_string += chr(int(s[i:i + 2], 16))
    ascii_string = ascii_string.encode('ascii')
    base64_bytes = base64.b64encode( ascii_string )
    print('/ascii:', ascii_string)
    return base64_bytes.decode('ascii')

res = encode_base64( xstr )
print('/encoded:', res)

assert res == comp

