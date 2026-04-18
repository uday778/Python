set1={32,32,21,45,67,21,89}
print(type(set1))
print(set1)  #unordered collection of unique elements
print(21 in set1)
print(len(set1))
print()
set2=set('abcdefu')
set3=set('aeiou')
print(type(set2))
print(set2)
print(set3)
print()
print()


print(set2-set3)  #difference
print(set2|set3)  #union
print(set2&set3)  #intersection
print(set2^set3)  #symmetric difference


