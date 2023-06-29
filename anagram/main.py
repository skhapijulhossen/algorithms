# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_alpha_freq, t_alpha_freq = dict(), dict()
        for x, y in zip(s, t):
            s_alpha_freq[x] = 1 + s_alpha_freq.get(x, 0)
            t_alpha_freq[y] = 1 + t_alpha_freq.get(y, 0)
        return s_alpha_freq == t_alpha_freq
