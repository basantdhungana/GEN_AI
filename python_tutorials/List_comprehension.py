# List Comprehension
# Definition:
# A concise and Pythonic way to create a new list by iterating
# over an iterable and optionally applying conditions.

'''syntax = [expression for item in iterable if condition]'''

# When to use:
# 1. When you need to create a new list from an existing iterable.
# 2. When the logic is simple and can be written in a single expression.
# 3. When you want shorter and more readable code than a traditional loop.
# 4. When filtering elements from a collection.
# 5. When transforming data (e.g., squaring numbers, converting text to uppercase).

# When NOT to use:
# 1. When the logic is complex and difficult to read in one line.
# 2. When multiple nested conditions make the code confusing.
# 3. When you are performing actions other than creating a list
#    (e.g., writing to a file, making API calls, logging).

a=["a","d","i","o"]



vowel_list =[char for char in a if char in "aeiou"]

print(vowel_list)


numbers = [1, 2, 3, 4, 5]

odd_list =[num for num in numbers if num %2 !=0]


print(odd_list)