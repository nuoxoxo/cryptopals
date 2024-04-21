hex1 = '1c0111001f010100061a024b53535009181c'

hex2 = '686974207468652062756c6c277320657965'

def hex_str_to_int_list(s: str):
    return [ int(s[i:i + 2], 16) for i in range(0, len(s), 2) ]

L = hex_str_to_int_list( hex1 )
R = hex_str_to_int_list( hex2 )

xor_str_list = [hex(l ^ r)[2:] for l, r in zip(L, R)]
xor_chr_list = [chr(int(l ^ r)) for l, r in zip(L, R)]

res = ''.join(xor_str_list)
msg = ''.join(xor_chr_list)

print('/result -', res)
print('/hidden -', msg)

assert res == '746865206b696420646f6e277420706c6179'

