import bisect

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        sub = []
        
        for _, h in envelopes:
            idx = bisect.bisect_left(sub, h)
            if idx == len(sub):
                sub.append(h)
            else:
                sub[idx] = h
                
        return len(sub)