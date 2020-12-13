class Solution(object):
    def isHappy(self, n):
        digits = self.get_digits(n)
        sum_dig = self.sum_of_squares(digits)
        if sum_dig == 1:
            return True
        else:
            self.isHappy(sum)

    def get_digits(self, n):
        result = []
        while n> 0:
            result.append(n%10)
            n = n//10
        return result

    def sum_of_squares(self, nums):
        result = 0
        for num in nums:
            result += num**2
        return result


print(Solution().isHappy(19))
