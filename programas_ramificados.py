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
name_1 = input("Enter your name: ")
age_1 = int(input("Enter your age "))

print("User 2")
print("*"*10)

name_2 = input("Enter your name:")
age_2 = int(input("Enter your age: "))

if age_1 > age_2:
    print(f"{name_1} is {age_1} years old and is older than {name_2} that is {age_2} years old")
elif age_1 == age_2:
        print(f"{name_1} and {name_2} are the same age, {age_2} years old")
else:
    print(f"{name_1} is {age_1} years old and is younger than {name_2} that is {age_2} years old")
    