# Given two lists `a = [1,2,3]` and `b = [4,5,6]`, create a new list with elements as sums of corresponding elements from a and b.

a = [1,2,3]
b = [4,5,6]


new_list=list(map(sum,zip(a,b)))
print(new_list)

# Given two lists `a = [1,2,3]` and `b = [4,5,6]`, create a new list with elements as sums of corresponding elements from a and b.

a = [1,2,3]
b = [4,5,6]


new_list=list(map(sum,zip(a,b)))
print(new_list)