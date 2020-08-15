target = int(input('Chose a value: '))
epsilon = 0.01
low = 0.0
high = max(1.0, target)
result = (high+low)/2
print(f'Low:{low}---High: {high}----Result: {result}----Result**2: {result**2} \n ')


while abs(result**2 - target) >= epsilon:
    if result**2 <= target:
        low = result
    else:
        high = result
    result = (high+low)/2
    print(f'Low:{low}---High: {high}----Result: {result}----Result**2: {result**2} \n ')
    

print(f'\n The squared root of {target} es {result}')