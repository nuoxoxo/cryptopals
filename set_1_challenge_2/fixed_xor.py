hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'

def hex_str_to_int_list(s: str):
    return [ int(s[i:i + 2], 16) for i in range(0, len(s), 2) ]

L, R = hex_str_to_int_list( hex1 ), hex_str_to_int_list( hex2 )
xor = [hex(l ^ r)[2:]  for l, r in zip(L, R)]
res = ''.join(xor)
res2 = ''.join([chr(int(l ^ r))  for l, r in zip(L, R)])
print('/res', res)
print('/hidden -', res2)
