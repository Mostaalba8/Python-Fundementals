# def find_target(nums, target) -> tuple:
#     temp_i = 0
#     temp_y = 0
#     for i in nums:
#         print(f'i = {temp_i}')
#         for y in nums:
#             print(f'---y = {temp_y}')
#             if i != y:
#                 if i + y == target:
#                     temp_tuple = (temp_i, temp_y)
#                     return temp_tuple
#             temp_y += 1
#         temp_y = 0
#         temp_i += 1



# refactored find_target
def finding_target(nums: int, target: int) -> tuple:
    # if type(target) is not (int or float):
    #     raise TypeError

    # for i in nums:
    #     if type(i) is not (int or float):
    #         raise TypeError

    result_tuple = None
    for first_index, first_value in enumerate(nums):
        for second_index, second_value in enumerate(nums):
            if first_value + second_value == target:
                temp_tuple = (first_index, second_index) if first_index != second_index else None
                result_tuple = temp_tuple
                return result_tuple
    if result_tuple is None:
        return 'Not found'



nums = (2, 7, 11, 16)

if finding_target(nums, 18) in [(0,3), (1,2), (2,1)]:
    print(True)

print(finding_target(nums, 18))
