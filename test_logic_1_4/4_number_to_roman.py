"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        base = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        if number <= 0:
            return "number can not less than or equal 0"
        elif number == 4000:
            return "MMMM"
        elif number > 4000:
            return ""
        
        num_list = list(map(lambda x: int(x), str(number)))
        power_list = range(len(num_list)-1, -1, -1)
        zip_num_power = zip(num_list, power_list)
        roman = ''
        for num, power in zip_num_power:
            digit = 10**power
            val = num * digit
            if val > 0 and val < 5*digit:
                if val != 4*digit:
                    time = int(val / digit)
                    roman += base[digit]*time
                else:
                    roman += base[digit]
                    roman += base[5*digit] 
            elif val >= 5*digit:
                if val != 9*digit:
                    roman += base[5*digit]
                    time = int((val-5*digit) / digit)
                    roman += base[digit]*time
                else:
                    roman += base[digit]
                    roman += base[val+digit]
        return roman
    
tests = [
    (
        (-1,),
        "number can not less than or equal 0",
    ),
    (
        (101,),
        "CI",
    ),
    (
        (1444,),
        "MCDXLIV",
    ),
    (
        (1646,),
        "MDCXLVI",
    ),
    (
        (3999,),
        "MMMCMXCIX",
    ),
]