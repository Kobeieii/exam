from utils.decorators import timing_decorator
"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    @timing_decorator
    def find_max_index(self, numbers: list) -> int | str:
        if len(numbers) == 0:
            return "list can not blank"
        
        max_num = None
        idx_max_num = None
        for idx, number in enumerate(numbers):
            if not max_num:
                max_num = number
                idx_max_num = idx
            if number > max_num:
                max_num = number
                idx_max_num = idx
        return idx_max_num
    
tests = [
    (
        ([],),
        "list can not blank",
    ),
    (
        ([1,2,3,4,5],),
        4,
    ),
    (
        ([5,4,3,2,1],),
        0,
    ),
    (
        ([1,2,3,60,4,5],),
        3,
    ),
]