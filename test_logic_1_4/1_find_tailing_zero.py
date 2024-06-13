from utils.decorators import timing_decorator
"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    @timing_decorator
    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        is_zero = False
        power = 1
        number_of_five = 0
        while not is_zero:
            res = number//(5**power)
            if res:
                power += 1
                number_of_five += res
            else:
                is_zero = True
        return number_of_five
            
tests = [
    (
        (-10,),
        "number can not be negative",
    ),
    (
        (1,),
        0,
    ),
    (
        (7,),
        1,
    ),
    (
        (10,),
        2,
    ),
    (
        (100,),
        24,
    ),
    (
        (1000,),
        249,
    )
]
