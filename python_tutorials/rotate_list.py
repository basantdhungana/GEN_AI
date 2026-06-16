# rotate_list.py

# rotate_list.py

def rotate_right(lst, k):
    k = k % len(lst)  # handle k > len(lst)
    return lst[-k:] + lst[:-k]

a = [1, 2, 3, 4, 5]

print(rotate_right(a, 2))