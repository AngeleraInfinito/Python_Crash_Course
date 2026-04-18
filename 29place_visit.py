# make a list of places and print it
places = ['germany', 'switzerland', 'north india', 'usa', 'japan']
print(places)
print('\n')

# sorted() to temporarily order list and print original one.
print(sorted(places))
print(places)
print('\n')

# sorted() to temporarily reverse order list and print original one.
print(sorted(places, reverse=True))
print(places)
print('\n')


# using reverse twice to change order of list and undoing it
places.reverse()
print(places)
places.reverse()
print(places)
print('\n')


# permanentaly sorting list in order and reverse order and printing it.
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print('\n')

