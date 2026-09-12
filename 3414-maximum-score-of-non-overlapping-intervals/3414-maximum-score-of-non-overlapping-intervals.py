from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        intervals = [
            (start, end, weight, i)
            for i, (start, end, weight) in enumerate(intervals)
        ]

        intervals.sort()

        n = len(intervals)

        starts = [interval[0] for interval in intervals]

        next_index = []

        for i in range(n):
            end = intervals[i][1]

            j = bisect_right(starts, end)
            next_index.append(j)

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            for k in range(1, 5):

               
                skip = dp[i + 1][k]

                next_i = next_index[i]

                weight = intervals[i][2]
                original_index = intervals[i][3]

                take_weight = weight + dp[next_i][k - 1][0]

                take_indices = sorted(
                    dp[next_i][k - 1][1] + [original_index]
                )

                take = (take_weight, take_indices)
                if take[0] > skip[0]:
                    dp[i][k] = take

                elif take[0] == skip[0]:
                    dp[i][k] = min(take, skip)

                else:
                    dp[i][k] = skip

        return dp[0][4][1]