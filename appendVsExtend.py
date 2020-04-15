import timeit

def append2x(foo):
    for a,b in enumerate(range(1, 100)):
        foo.append(a)
        foo.append(b)

def extend_lst(foo):
    for a,b in enumerate(range(1, 100)):
        foo.extend([a,b])

def extend_tup(foo):
    for a, b in enumerate(range(1, 100)):
        foo.extend((a, b))


l1 = []
l2 = []
l3 = []

print timeit.timeit('append2x(l1)',setup = 'from __main__ import append2x,l1')
print timeit.timeit('extend_lst(l2)',setup = 'from __main__ import extend_lst,l2')
print timeit.timeit('extend_tup(l3)',setup = 'from __main__ import extend_tup,l3')

# 28.8662294
# 29.0121452
# 21.3474822
