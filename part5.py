

# squares = {n: n*n for n in range(50)}
#
# print(squares)

# countries = ['England', 'Norway', 'Bulgaria', 'Germany', 'Netherlands', 'Spain']
# first_letters = [c[0:3] for c in countries]
# print(first_letters)

num = [1,2,2,3]
# print(sum(num))
# print(min(num))
# print(max(num))




def sum_of_squared_list(list):
    squared = [n*n for n in list]
    if squared == []:
        return 0
    else:
        return sum(squared)


def multiple_of_5(a_val):
    return a_val * 5

def apply(items, f) -> list:
    new_list = []
    for item in items:
        new_val = f(item)
        new_list.append(new_val)
    return new_list


print(sum_of_squared_list(num))
print(apply(num, f=multiple_of_5))
