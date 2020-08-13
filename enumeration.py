target = int(input("Entry a value:"))
result = 0

while result**2 < target:
    result += 1

if result**2 == target:
    print(f'The squared root of {target} is: {result}')
else:
    print(f'The value: {target} don´t have squared root perfect')