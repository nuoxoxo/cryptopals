# DIY base64 encoding

# this is a helper
def binStr_to_base64(bs: str) -> str:
    N = len(bs)
    # special operation 1 - append zeros to make len multiple of 6
    if N % 6 != 0:
        bs += '0' * (6 - N % 6)
    res = ''
    b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in range(0, N, 6):
        idx = int(bs[i:i + 6], 2)
        # print('test/', int(bs[i:i + 6],2))
        res += b64[idx]
    N = len(res)
    if N % 4 != 0:
        res += '=' * (4 - N % 4)
    # special operation 2 - append ='s to make len(res) mult of 4
    return res
 

def asciiStr_to_base64(s: str) -> str:
    bs = ''
    for c in s:
        o = ord(c)
        bs += bin(o)[2:].zfill(8)
    return binStr_to_base64(bs)

# also, hex to base64

def hexStr_to_base64(s: str) -> str:
    assert len(s) % 2 == 0
    bs = ''
    for i in range(0, len(s), 2):
        bc = bin(int(s[i:i + 2], 16))[2:].zfill(8)
        bs += bc
    return binStr_to_base64(bs)


# test drive

if __name__ == '__main__':
    r1 = asciiStr_to_base64('And')
    print('r1/', r1)

    r2 = asciiStr_to_base64('g')
    print('r2/', r2)

    r3 = asciiStr_to_base64('gm')
    print('r3/', r3)

    assert r1 == 'QW5k'
    assert r2 == 'Zw=='
    assert r3 == 'Z20='

