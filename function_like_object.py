def multiply_for_two(n):
    return n*2

def add_two(n):
    return n+2

def apply_operations(f,numbers):
    resultados = []
    for number in numbers:
        resultado = f(number)
        resultados.append(resultado)
    return resultados
i = 0 
numbers = []
while i < 5:
    value = int(input("Entre a value: "))
    if value < 1000:
        numbers.append(value)
        i += 1
    else:
        print("Please enter a number")


resultados = apply_operations(add_two, numbers)
for resultado in resultados:
    print(resultado)