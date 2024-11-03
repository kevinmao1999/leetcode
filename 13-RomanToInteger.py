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
