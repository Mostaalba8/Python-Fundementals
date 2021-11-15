# def find_target(nums, target) -> tuple:
#     temp_i = 0
#     temp_y = 0
#     for i in nums:
#         print(f'i = {temp_i}')
#         for y in nums:
#             print(f'---y = {temp_y}')
#             if i != y:
#                 if i + y == target:
#                     temp_tuple = (temp_i,temp_y)
#                     return temp_tuple
#                     break
#             temp_y += 1
#         temp_y = 0
#         temp_i += 1

# refactored find_target
def find_target(nums: int, target: int) -> tuple:
    for first_index, first_value in enumerate(nums):
        for second_index, second_value in enumerate(nums):
            if first_value + second_value == target:
                temp_tuple = (first_index, second_index) if first_index != second_index else None
                return temp_tuple


nums = (2, 7, 11, 15)
print(find_target(nums, 18))