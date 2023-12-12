import itertools

c = ['0','1','-1']

x = itertools.product(c,repeat=2)

for item in x:
    print(item)
