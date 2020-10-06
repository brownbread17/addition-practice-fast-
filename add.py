from random import randint

digits = int(input('What do you want to practice? '))


def two_digit():
    while True:
        a = randint(10, 99)
        b = randint(10, 99)
        print(a, b)
        lol = a + b
        a = int(input('Your answer: '))
        if a == lol:
            print('correct')
        else:
            print('lag gye')

        choice = input("continue? (y/n)").lower()
        if choice == "y":
            continue
        else:
            break


def three_digit():
    while True:
        a = randint(100, 999)
        b = randint(100, 999)
        print(a, b)
        lol = a + b
        a = int(input('Your answer: '))
        if a == lol:
            print('correct')
        else:
            print('lag gye')

        choice = input("continue? (y/n)").lower()
        if choice == "y":
            continue
        else:
            break


if digits == 2:
    two_digit()

elif digits == 3:
    three_digit()

else:
    print('Bye!')
