def Options():
    print('Select with wich algorithm you want to resolve the problem \n')
    option = int(input(' 1. Aproximations\n 2. Binary Search\n 3. Enumeration \n Entry:'))
    if option == 1:
        Aproximations()
    elif option == 2:
        Binary_search()
    elif option == 3:
        Enumeration()
    else:
        print('Error, pleas entry a valid number')
        print('*'*100)
        Options()

    return 0
# print(Options())

def Enumeration():
    print('You have selected Enumeration Algorithm')
    target = int(input("Entry a value:"))
    result = 0

    while result**2 < target:
        result += 1

    if result**2 == target:
        print(f'The squared root of {target} is: {result}')
    else:
        print(f'The value: {target} don´t have squared root perfect')

    return 0

def Binary_search():
    print('You have selected Binary search Algorithm')
    target = int(input('Chose a value: '))
    epsilon = 0.01
    low = 0.0
    high = max(1.0, target)
    result = (high+low)/2
    # print(f'Low:{low}---High: {high}----Result: {result}----Result**2: {result**2} \n ')


    while abs(result**2 - target) >= epsilon:
        if result**2 <= target:
            low = result
        else:
            high = result
        result = (high+low)/2
        # print(f'Low:{low}---High: {high}----Result: {result}----Result**2: {result**2} \n ')
    print(f'\n The squared root of {target} es {result}')

    return 0

def Aproximations():
    print('You have selected Aproximations Algorithm')
    target = int(input('Entry the value:'))
    epsilon = 0.01
    step = epsilon**2
    result = 0.0

    while abs(result**2 -target) >= epsilon and result <= target :
        # print(f'{result**2 -target}',result)
        result += step

    if abs(result**2) == target >= epsilon:
        print('The squared root couldnt be found')
    else:
        print(f'The squared root is: {result}')

    return 0



print('Welcome, this program calculate the squared root of any value \n And you can select the algorithm that gonna be used.')
print('*'*100)
Options()