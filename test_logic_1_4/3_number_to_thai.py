from utils.decorators import timing_decorator
"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    @timing_decorator
    def number_to_thai(self, number: int) -> str:
        base = {
            '0': "",
            '1': "หนึ่ง",
            '2': "สอง",
            '3': "สาม",
            '4': "สี่",
            '5': "ห้า",
            '6': "หก",
            '7': "เจ็ด",
            '8': "แปด",
            '9': "เก้า",
        }

        digits = {
            1:"",
            10: "สิบ",
            100: "ร้อย",
            1000: "พัน",
            10000: "หมื่น",
            100000: "แสน",
            1000000: "ล้าน",
        }

        if number < 0:
            return "number can not less than 0"
        elif number == 0:
            return "ศูนย์"
        elif number == 1:
            return "หนึ่ง"
        elif number == 10000000:
            return "สิบล้าน"
        
        num_copy = number
        power_of_num = 0
        while num_copy != 0:
            num_copy //= 10
            if num_copy != 0:
                power_of_num += 1

        thai_word = ""
        num_str = str(number)
        for power in range(power_of_num, -1, -1):
            first_num = str(num_str)[0]
            digit = digits[10**power]
            prefix = base[first_num]
            
            if digit == 'สิบ':
                if first_num=='2':
                    prefix = 'ยี่'
                elif first_num=='1':
                    prefix = ''
            elif digit == '':
                if first_num=='1':
                    prefix = 'เอ็ด' 
            
            thai_word += f"{prefix}{digit}" if first_num != '0' else ""
            if len(num_str) > 1:
                num_str = str(num_str)[1:]
        
        return thai_word
    
tests = [
    (
        (-1000,),
        "number can not less than 0",
    ),
    (
        (123,),
        "หนึ่งร้อยยี่สิบสาม",
    ),
    (
        (5348000,),
        "ห้าล้านสามแสนสี่หมื่นแปดพัน",
    ),
    (
        (348020,),
        "สามแสนสี่หมื่นแปดพันยี่สิบ",
    ),
    (
        (10000000,),
        "สิบล้าน",
    ),
    (
        (9999999,),
        "เก้าล้านเก้าแสนเก้าหมื่นเก้าพันเก้าร้อยเก้าสิบเก้า",
    ),
    (
        (11,),
        "สิบเอ็ด",
    ),
    (
        (2,),
        "สอง",
    ),
]

        
        
