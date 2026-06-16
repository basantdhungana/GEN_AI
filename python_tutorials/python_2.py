# Lists, Dictionaries, Tuples, and Sets

# Lists
# A list is a mutable, ordered collection of items.
fruits = ["apple", "banana", "cherry","pratik",1,1.5]
print("List of fruits:", fruits)

# Adding an item to the list
# fruits.append("orange")
# print("After appending an item:", fruits)

# # Removing an item from the list
fruits.remove("banana")
print("After removing an item:", fruits)

# Accessing elements by index
print("First fruit:", fruits[0])

# Dictionaries
# A dictionary is a mutable, unordered collection of key-value pairs.
person = {"name": "Alice", "age": 25, "city": "New York"}
print("\nDictionary:", person)

# Accessing a value by key
print("Name:", person["name"])

# Adding a new key-value pair
person["job"] = "Engineer"
print("After adding a new key-value pair:", person)

# Removing a key-value pair
del person["age"]
print("After removing a key-value pair:", person)

# Tuples
# A tuple is an immutable, ordered collection of items.
coordinates = (10, 20, 30)
print("\nTuple of coordinates:", coordinates)

# Accessing elements by index
print("First coordinate:", coordinates[0])

# Sets
# A set is a mutable, unordered collection of unique items.
numbers = {1, 2, 3, 4, 5}
print("\nSet of numbers:", numbers)

# Adding an item to the set
numbers.add(6)
print("After adding an item:", numbers)

# Removing an item from the set
numbers.remove(3)
print("After removing an item:", numbers)

# Demonstrating the difference between sets and lists
# Sets do not allow duplicate items
duplicate_set = {1, 2, 2, 3}
print("\nSet with duplicates (duplicates are removed):", duplicate_set)

# Lists allow duplicate items
duplicate_list = [1, 2, 2, 3]
print("List with duplicates:", duplicate_list)