class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        if not digits:
            return []

        digit_to_letters = [
            "abc",   
            "def",  
            "ghi",  
            "jkl",   
            "mno",   
            "pqrs",  
            "tuv",   
            "wxyz"   
        ]

        result = [""]
        for digit in digits:
    
            letters = digit_to_letters[int(digit) - 2]
          
            result = [existing + letter 
                     for existing in result 
                     for letter in letters]
      
        return result
