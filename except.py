def divide_element_in_list(array_number, divisor):
    try:
        return [i / divisor for i in array_number]
    except ZeroDivisionError as e:
        print(e)
        return array_number


array_number = list(range(10))
divisor = 0


print( divide_element_in_list(array_number, divisor))

    