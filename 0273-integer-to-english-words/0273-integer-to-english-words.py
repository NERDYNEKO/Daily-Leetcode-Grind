class Solution:
    def numberToWords(self, num: int) -> str:
        a = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }

        if num == 0:
            return "Zero"
        
        result_parts = []

        # Handle billions
        billions = num // 1000000000
        if billions > 0:
            result_parts.append(self.helper(billions) + " Billion")

        # Handle millions
        millions = (num % 1000000000) // 1000000
        if millions > 0:
            result_parts.append(self.helper(millions) + " Million")

        # Handle thousands
        thousands = (num % 1000000) // 1000
        if thousands > 0:
            result_parts.append(self.helper(thousands) + " Thousand")

        # Handle remainder (1-999)
        remainder = num % 1000
        if remainder > 0:
            result_parts.append(self.helper(remainder))

        return " ".join(result_parts)

    def helper(self, i: int) -> str:
        a = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"}

        # number 1-19
        if 0 <= i <= 19:
            return a[i]

        # number between 20-99
        if 20 <= i <= 99:
            tens = (i // 10) * 10
            ones = i % 10
            if ones == 0:
                return a[tens]
            else:
                return a[tens] + " " + a[ones]

        # number between 100-999
        if 100 <= i <= 999:
            hundred = i // 100
            result = a[hundred] + " Hundred"
            remainder = i % 100
            if remainder == 0:
                return result
            else:
                return result + " " + self.helper(remainder)