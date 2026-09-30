class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        reslt = [0] * len(seq)
        depth = 0

        for index, char in enumerate(seq):
            if char == "(":
                reslt[index] = depth & 1

                depth += 1
            else: 
                depth -= 1
                reslt[index] = depth & 1
      
        return reslt
