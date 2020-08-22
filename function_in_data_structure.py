def apply_operation(n):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones :
        resultado.append(operacion(n))

    return resultado
n = -8
print(apply_operation(n))