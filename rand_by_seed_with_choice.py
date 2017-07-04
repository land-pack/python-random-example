import random

choice = [1,2,3,4,5,6]

random.seed(10101)

d1 = set()
for i in range(100):
    k= random.choice(choice)
    print('i={}---k={}'.format(i,k))
    d1.add(k)

print d1

# reset seed
random.seed(10101)
d2 = set()
for i in range(100):
    k= random.choice(choice)
    print('i={}---k={}'.format(i,k))
    d2.add(k)

print d2


d3 = d2 | d1

print d3 

