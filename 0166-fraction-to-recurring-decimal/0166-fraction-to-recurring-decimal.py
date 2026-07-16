class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
            
        res = []
        
        # Handle signs
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
            
        num = abs(numerator)
        den = abs(denominator)
        
        # Integral part
        res.append(str(num // den))
        num %= den
        
        if num == 0:
            return "".join(res)
            
        # Fractional part
        res.append(".")
        remainder_map = {}
        
        while num != 0:
            if num in remainder_map:
                res.insert(remainder_map[num], "(")
                res.append(")")
                break
                
            remainder_map[num] = len(res)
            num *= 10
            res.append(str(num // den))
            num %= den
            
        return "".join(res)