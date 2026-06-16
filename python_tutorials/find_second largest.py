'''Implement a function to find the second largest element in a list without sorting the entire list.'''

def second_largest(lst):
    if len(lst) < 2:
        return None

    first = second = float('-inf')

    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return None if second == float('-inf') else second

print(second_largest([10, 20, 4, 45, 99]))