# 
def longet_adjacent_k_group(s: str, k: int) -> dict:
    out = dict()
    if len(s)<=2 or k==0:
        return dict()
    idx = 1
    count = 1
    while idx < len(s):
        if s[idx] != s[idx-1]:
            if count >= k:
                out[s[idx-1]] = count
            count = 0
        count += 1
        idx += 1
    else:
        if count >= k:
            out[s[idx-1]] = count
    return out


if __name__ == '__main__':
    # input : s= aaabbcdbbbb k=4
    # output : {b:4}

    # input : s= aaabbcdbbbb k=3
    # output : {a:3, b:4}

    # input : s= acabbcbbaaa k=3
    # output : {a:3}

    strings = [("aaabbcdbbbb",4), ("aaabbcdbbbb", 3), ("acabbcbbaaa", 3)]
    for s, k in strings:
        out = longet_adjacent_k_group(s, k=k)
        print(f'Output for {s}: {out}')