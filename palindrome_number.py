class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_num = x
        reverse_num = 0

        while x > 0:
            last_digit = x % 10
            reverse_num = reverse_num * 10 + last_digit
            x = x // 10

        return temp_num == reverse_num 

        