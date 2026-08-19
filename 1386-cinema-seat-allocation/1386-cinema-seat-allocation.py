class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:

        rows = {}
        for r, seat in reservedSeats:
            if r not in rows:
                rows[r] = 0
            if 2 <= seat <= 9:
                rows[r] |= 1 << (seat - 2)
        ans = (n - len(rows)) * 2

        for mask in rows.values():

            left = 0b00001111
            middle = 0b00111100
            right = 0b11110000

            if mask & left == 0:

                if mask & right == 0:
                    ans += 2
                else:
                    ans += 1

            elif mask & right == 0:
                ans += 1

            elif mask & middle == 0:
                ans += 1

        return ans