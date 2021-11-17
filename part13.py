import math
from typing import Optional, List

#functions below are copied from other parts to test out

#from part8.py
def square_root(n: int) -> int:
    if n >= 0:
        return math.sqrt(n)
    else:
        raise ValueError

#from part7.py
def finding_target(nums: List[int], target: int) -> Optional[tuple]:
    for first_index, first_value in enumerate(nums):
        for second_index, second_value in reversed(enumerate(nums)):
            if (first_index != second_index) and (first_value + second_value == target):
                return (first_index, second_index)
    return None

