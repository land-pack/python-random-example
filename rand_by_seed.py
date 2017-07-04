import random


random.seed(10101)

d1 = set()
for i in range(100):
    k= random.random()
    d1.add(k)

print(len(d1))

# reset seed
random.seed(10101)
d2 = set()
for i in range(100):
    k= random.random()
    d2.add(k)

print(len(d2))


d3 = d2 | d1

print(len(d3))

