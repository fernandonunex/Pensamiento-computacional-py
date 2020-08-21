import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

def factorial(n):
    """This function compute the factorial of n

    Args:
        n ([int]): [any number integer > 0]
        return n!
    """
    if n ==1:
        return 1
    print(f'The value of n: {n} \n')
    return n*factorial(n-1)

# n = int(input('Enter a number to find its factorial: '))
# print(f'The factorial of is: {factorial(n)}')