a=[1,2,3,4,'hi']

t=tuple(a)

print(t)

try:
    t[0] = 10
    print("Mutable")
except TypeError:
    print("Immutable")