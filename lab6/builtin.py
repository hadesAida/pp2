# 1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)


nums = [2, 3, 4, 5]
print(multiply_list(nums)) 
# 2
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return {"Uppercase": upper, "Lowercase": lower}

text = "Hello World!"
print(count_case(text)) 
#
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar")) 
print(is_palindrome("hello"))  
# 4
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    return math.sqrt(number)


num = 25100
delay = 2123
result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")


# 5
def all_true(tup):
    return all(tup)

t1 = (True, True, True)
t2 = (True, False, True)
print(all_true(t1))  
print(all_true(t2))  


