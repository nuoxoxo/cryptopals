def Solution_intuition (L: bytes, R: bytes) -> int:
    assert len(L) == len(R)
    lones, rones = 0, 0
    N = len(L)
    res = 0
    for l, r in zip(L, R):
        res += bin(ord(l) ^ ord(r)).count('1')
    return res

def Solution_and_one_right_shift (L: bytes, R: bytes) -> int:
    def count_one_in_bin(byte: bytes) -> int:
        res = 0
        while byte != 0:
            res += byte & 1
            byte >>= 1
        return res
    res = 0
    for l, r in zip(L, R):
        res += count_one_in_bin ( ord(l) ^ ord(r) )
    return res



if __name__ == '__main__':

    Solutions = [
        Solution_and_one_right_shift,
        Solution_intuition,
    ]

    s1, s2 = 'this is a test', 'wokka wokka!!!'
    for f in Solutions:
        res = f( s1, s2 )
        print( res, res == 37 )

