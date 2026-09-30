class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        reslt = [0] * len(seq)
        depth = 0

        for i, j in enumerate(seq):
            if j== "(":
                reslt[i] = depth & 1

                depth += 1
            else: 
                depth -= 1
                reslt[i ]= depth & 1
      
        return reslt
