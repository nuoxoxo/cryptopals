# trying to decode base64 encoded strings

def base64_to_asciiStr(s: str) -> str:
    b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    bs = ''
    for c in s:
        if c == '=':
            continue
        idx = b64.index(c)
        bc = bin(idx)[2:].zfill(6)
        bs += bc
    N = len(bs)
    if N % 8 != 0:
        bs = bs[:N - N % 8]
    res = ''
    for i in range(0, len(bs), 8):
        trunk = bs[i:i + 8]
        res += chr(int(trunk, 2))
    return res

r1 = base64_to_asciiStr('QW5k')
print('r1/', r1)

r2 = base64_to_asciiStr('Zw')
print('r2/', r2)

r3 = base64_to_asciiStr('Z20')
print('r3/', r3)

assert r1 == 'And'
assert r2 == 'g'
assert r3 == 'gm'
