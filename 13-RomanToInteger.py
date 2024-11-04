# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
#     1 <= s.length <= 15
#     s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#     It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt1(self, s: str) -> int:
        prev = ""
        val = 0

        # loop over each char in the string starting from the front
        for i in range(len(s)):
            match s[i]:
                # if M add 1000 - if CM add 900-100=800
                case "M":
                    if prev == "C":
                        val += 800
                    else:
                        val += 1000
                    prev = "M"
                # if D add 500 - if CD add 400-100=300
                case "D": # 
                    if prev == "C":
                        val += 300
                    else:
                        val += 500
                    prev = "D"
                # if C add 100 - if XC add 90-10=80
                case "C":
                    if prev == "X":
                        val += 80
                    else:
                        val += 100
                    prev = "C"
                # if L add 50 - if XL add 40-10=30
                case "L":
                    if prev == "X":
                        val += 30
                    else:
                        val += 50
                    prev = "L"
                # if X add 10 - if IX add 9-1=8
                case "X":
                    if prev == "I":
                        val += 8
                    else:
                        val += 10
                    prev = "X"
                # if V add 5 - if IV add 4-1=3
                case "V":
                    if prev == "I":
                        val += 3
                    else:
                        val += 5
                    prev = "V"
                # if I add 1
                case "I":
                    val += 1
                    prev = "I"
        return val
    
    def romanToInt2(self, s: str) -> int:
        # dictionary of roman numerals and associated values
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        length = len(s)

        # loop over each numeral
        for i in range(length):
            # if the numeral is not the very last AND it is of a lesser value than the next, that means we have a special case
            if i < length-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                total -= roman_dict[s[i]]
            else:
                total += roman_dict[s[i]]
        return total
