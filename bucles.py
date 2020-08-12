i

week = ['M','T','W','T','F','S','S']
iterator = iter(week)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)

students = {
    'Mexico': 80,
    'United stated':40,
    'Spain': 14,
}

""" for country in students:
    print(country)

for country in students.keys():
    print(country) """

for number_of_students in students.values():
    print(number_of_students)

for number_of_students, country in students.items():
    print( country, number_of_students)


    