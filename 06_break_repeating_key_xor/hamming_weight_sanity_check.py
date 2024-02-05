def hamming_weight_2_strings (L: str, R: str) -> int:
    assert len(L) == len(R)
    lones, rones = 0, 0
    N = len(L)
    res = 0
    for i in range(N):
        res += bin(ord(L[i]) ^ ord(R[i])).count('1')
    return res

res = hamming_weight_2_strings ('this is a test', 'wokka wokka!!!')
print(res, res == 37)
    
