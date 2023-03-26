

def get_longest_k_distinct_subtring(s, k=2) -> int:
    if k<2 or len(s)<=2:
        return 0
    sidx, eidx = 0, 0
    out = 0
    seen = dict()
    while eidx < len(s):
        if s[eidx] not in seen:
            k -= 1
        seen[s[eidx]] = eidx

        if k<0:
            minn = min(seen.values())
            sidx = minn + 1
            i = list(seen.values()).index(minn)
            key = list(seen.keys())[i]
            seen.pop(key)
            k += 1

        out = max(out, eidx - sidx + 1)
        eidx += 1 
    return out








if __name__ == '__main__':
    #Input: Str = “aabbcc”, k = 1
    #Output: 2
    #Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.
    #
    #Input: Str = “aabbcc”, k = 2
    #Output: 4
    #Explanation: Max substring can be any one from {“aabb” , “bbcc”}.
    #
    #Input: Str = “aabbcc”, k = 3
    #Output: 6
    #Explanation: 
    #There are substrings with exactly 3 unique characters
    #{“aabbcc” , “abbcc” , “aabbc” , “abbc” }
    #Max is “aabbcc” with length 6.
    #
    #Input: Str = “aaabbb”, k = 3
    #Output: Not enough unique characters
    #Explanation: There are only two unique characters, thus show error message. 

    strings = [("aabbcc",1), ("aabacccac", 2), ("aaabbb", 2), ('aadse', 0)]
    for s, k in strings:
        out = get_longest_k_distinct_subtring(s, k=k)
        print(f'Output for {s}: {out}')