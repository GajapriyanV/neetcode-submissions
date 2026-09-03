class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        carry = 1
        while carry and i >= 0:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
        
        if carry:
            digits = [1] + digits

        