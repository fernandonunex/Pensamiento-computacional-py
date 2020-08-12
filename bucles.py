""" week = ['M','T','W','T','F','S','S']

for day in week:
    print(f"The day is {day}") """

""" iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario """

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
