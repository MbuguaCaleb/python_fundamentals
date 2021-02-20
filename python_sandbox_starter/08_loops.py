# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Caleb', 'Mercy', 'Wanjiru']

# simple for loop
# similar to javascript ES6
# for person in people:
#     print(f'Current Person: {person}')


# Break out of loop
# for person in people:
#     if person == 'Mercy':
#         break
#     print(f'current person in {person}')

# Continue
# for person in people:
#     if person == 'Mercy':
#         continue
#     print(f'current person in {person}')


# range
# Its very similar to a standard for loop
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f'Count:{count}')
    count += 1
