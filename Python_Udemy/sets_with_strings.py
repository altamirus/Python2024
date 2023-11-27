# Sets com strings
#
#
# from sets import set

s1 = {'a', 'b', 'c', 'd'}
s2 = {'e', 'f', 'c', 'd'}
s3 = {'a', 'b', 'g', 'h'}

s4 = s1.union(s2)
s5 = s1.intersection(s2)
s6 = s2.union(s3)
s7 = s2.difference(s3)

print(s4)
print(s5)
print(s6)
print(s7)
