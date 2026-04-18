# mom dad issac nikolo zuckerburg elon erik

# Invite people
people = ['mom', 'dad', 'erik']
print(people[0].title() + ' you are invited to dinner.')
print(people[1].title() + ' you are invited to dinner.')
print(people[2].title() + ' you are invited to dinner.')
print('\n')

# someone can't make it.
print(people[2].title() + " can't make it.")

# replacing that someone name.
people[2] = "elon"

# new set of invitations.
print(people[0].title() + ' you are invited to dinner.')
print(people[1].title() + ' you are invited to dinner.')
print(people[2].title() + ' you are invited to dinner.')
print('\n')

# new table
print("I found a bigger table everyone.")
people.insert(0, 'nikolo')
people.insert(2, 'issac')
people.append('zuckerburg')
print('\n')

# printing invitations part 2
print(people[0].title() + ' you are invited to dinner.')
print(people[1].title() + ' you are invited to dinner.')
print(people[2].title() + ' you are invited to dinner.')
print(people[3].title() + ' you are invited to dinner.')
print(people[4].title() + ' you are invited to dinner.')
print(people[5].title() + ' you are invited to dinner.')
print('\n')

# shrinking guest list
print('I can invite only two people for dinner.')

# removing people from list and telling them
pop_person_1 = people.pop(0)
print(pop_person_1 + ", I am sorry i can’t invite you to dinner.")

pop_person_2 = people.pop(1)
print(pop_person_2 + ", I am sorry i can’t invite you to dinner.")

pop_person_3 = people.pop(2)
print(pop_person_3 + ", I am sorry i can’t invite you to dinner.")

pop_person_4 = people.pop(-1)
print(pop_person_4 + ", I am sorry i can’t invite you to dinner.")

# invitations part -3
print(people[0] +  ' you are invited to dinner.')
print(people[1] +  ' you are invited to dinner.')

# rermoving everyone from list
del people[0]
del people[0]

# making sure list is empty by printing it.
print(people)
