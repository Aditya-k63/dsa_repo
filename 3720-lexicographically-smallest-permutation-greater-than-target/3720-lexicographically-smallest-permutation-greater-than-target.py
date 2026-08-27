from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        if n != len(target):
            return ""
        
        counts = Counter(s)
        max_match = 0
        while max_match < n and counts[target[max_match]] > 0:
            counts[target[max_match]] -= 1
            max_match += 1
        for i in range(max_match, -1, -1):
            if i < n:
                for code in range(ord(target[i]) + 1, ord('z') + 1):
                    c = chr(code)
                    if counts[c] > 0:
                        counts[c] -= 1
                        suffix = []
                        for ch_code in range(ord('a'), ord('z') + 1):
                            ch = chr(ch_code)
                            if counts[ch] > 0:
                                suffix.append(ch * counts[ch])
                        
                        return target[:i] + c + "".join(suffix)
            if i > 0:
                counts[target[i - 1]] += 1
                
        return ""
        