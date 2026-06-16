''' Remove duplicates from a list using a set, then convert back to list preserving order? (Note: sets don't preserve order in older Python). '''

def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

a = [1, 2, 2, 3, 1, 4, 5, 4]

print(remove_duplicates(a))
