"""Demo: show differences between shallow and deep copies of nested lists.

This module demonstrates shallow vs deep copying using a nested list.
Run this script to print examples showing how changing a shallow copy
can affect the original while a deep copy remains independent.
"""
import copy

def show_copy():
    # Original nested list
    original = [[1, 2, 3], [4, 5, 6]]
    
    # Shallow Copy
    shallow = original.copy()          # or copy.copy(original)
    
    # Deep Copy
    deep = copy.deepcopy(original)
    
    print("Original :", original)
    
    # Modify nested list
    shallow[0][0] = 99
    
    print("After change:")
    print("Original :", original)   # ← Changed!
    print("Shallow   :", shallow)   # ← Changed!
    print("Deep      :", deep)      # ← Not changed!
show_copy()
# Shallow Copy:
# - Fast
# - Only top level is copied
# - Nested lists/dicts are shared (reference)
# - Changing nested value affects original

# Deep Copy:
# - Slower (copies everything recursively)
# - Fully independent copy
# - Changing anything in deep copy does NOT affect original
# import copy

def show_copy():
    # Original list with nested list inside
    original = [[1, 2, 3], [4, 5, 6]]
    
    # Shallow Copy - only copies top level, nested objects are shared
    shallow = original.copy()        # or copy.copy(original)
    
    # Deep Copy - creates completely new copy of everything
    deep = copy.deepcopy(original)
    
    print("Before any change:")
    print("Original :", original)
    print("Shallow  :", shallow)
    print("Deep     :", deep)
    print("-" * 40)
    
    # Now changing value in shallow copy
    shallow[0][0] = 99          # Changing nested value
    shallow[1] = [7, 8, 9]      # Changing entire inner list
    
    print("After modifying shallow copy:")
    print("Original :", original)   # ← Affected by nested change
    print("Shallow  :", shallow)    # ← Changed
    print("Deep     :", deep)       # ← Not affected
    print("-" * 40)
    
    # Can I change value in all?
    # Yes - but behavior is different:
    # 1. Changing nested items → affects Original & Shallow
    # 2. Changing top level → only affects that copy
    # 3. Deep copy remains completely safe and independent

show_copy()