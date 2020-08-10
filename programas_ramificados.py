""" 2 == 3
2 != 3
2 > 3
2 < 3
2 <= 3
2 >= 3

True and True
False or True
not True

if expression:
    pass
elif expression:
    pass
else:
    pass """

num1 = int(input("Enter a number bigger than the next: "))
num2 = int(input("Enter a number smaller than the before: "))

if num1 > num2:
    print(f"The {num1} is bigger than {num2}")
else:
    print(f"The {num1} is´nt bigger than {num2}")