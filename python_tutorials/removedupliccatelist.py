'''Write a function that takes a list and returns a new list with duplicates removed while preserving the original order.'''

def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))