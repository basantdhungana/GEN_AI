''' Given `t = (1, 2, 3, 4, 5)`, unpack it into variables a, b, *rest.'''


t = (1, 2, 3, 4, 5)

a,b,*rest=t

print(a,b,rest)