from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        
        # Check palindrome feasibility (at most one character with an odd count)
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid = odd_chars[0] if odd_chars else ""
        
        # Build the pool of characters available for the first half
        half_counts = {ch: cnt // 2 for ch, cnt in counts.items() if cnt // 2 > 0}
        n = len(s)
        half_len = n // 2
        
        res = []
        
        def can_form_greater(idx: int, is_greater: bool) -> bool:
            if idx == half_len:
                full_s = "".join(res) + mid + "".join(reversed(res))
                return is_greater or full_s > target
            
            # Try available characters in sorted order
            for ch in sorted(half_counts.keys()):
                if half_counts[ch] == 0:
                    continue
                
                # If we are not yet strictly greater, don't pick smaller than target[idx]
                if not is_greater and ch < target[idx]:
                    continue
                
                half_counts[ch] -= 1
                res.append(ch)
                
                new_greater = is_greater or (ch > target[idx])
                if can_form_greater(idx + 1, new_greater):
                    return True
                
                res.pop()
                half_counts[ch] += 1
                
            return False

        if can_form_greater(0, False):
            return "".join(res) + mid + "".join(reversed(res))
        
        return ""