family = ['mother', 'father', 'brother', 'sister']
print(family)

# accessing elements in a list
print(family[0])

# concantentation
print("I love my " + family[0])

# replace
family[-1] = 'grandpa'
print(family)

# append
family.append('grandma')
print(family)

# insert
family.insert(-1, 'variable')
print(family)

# del statement
del family[-2]
print(family)

# pop method
popped_person = family.pop(-1)
print(family)

# remove
family.remove('grandpa')

# sort and sorted
print(sorted(family))
family.sort
print(family)

# reverse
family.reverse()
print(family)

# family members counting
print(len(family))
