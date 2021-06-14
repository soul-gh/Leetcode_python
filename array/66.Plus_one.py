class Solution:
    def plusOne(digits):
        N = len(digits)
        for i in range(N-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            elif i != 0 and digits[i] == 9:
                digits[i] = 0
                continue
            elif i == 0 and digits[i] == 9:
                digits[i] = 1
                digits.append(0)
        return digits
a = [9,9,9,9]
print(Solution.plusOne(a))