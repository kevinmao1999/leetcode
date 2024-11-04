# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:
# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    # solution1 converts to a string then runs a loop to compare chars to the opposite char based on index
    # runs in O(n) time, needing one loop over each char
    def isPalindrome1(self, x: int) -> bool:
        string = str(x)
        length = len(string)

        # for each char in the converted int, if it is not equal to the char on the opposite side, return False
        for i in range(length):
            if string[i] != string[length-1-i]:
                return False
        return True

    # solution2 directly manipulates the integer with the modulos operator to reverse it, then compares if it is the same backwards
    # still runs in O(n) time however since we only reverse half of the int (because the other half should be the same) it runs faster than solution1
    def isPalindrome2(self, x: int) -> bool:
        # if x is negative OR x is only 1 digit, return False
        if x < 0 or (x and x % 10 == 0):
            return False

        # get reverse of x - loop until rev matches x
        # for each loop, rev*10 to make room for a new ones digit
        # 12345
        # revs:
        # 0
        # 0*10 + 12345%10 = 0 + 5 
        # 5*10 + 1234%10 = 0 + 5
        # 54*10 + 123%10 = 0 + 5
        # 543*10 + 12%10 = 0 + 5
        rev = 0
        while rev < x:
            rev = rev * 10 + x % 10
            x //= 10

        if x == rev or x == rev//10:
            return True
        return False     
