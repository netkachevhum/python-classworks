import random


def verifier(a,b):
    c = 0
    if a==b:
        c = 0
    elif a>b:
        c = 1
    elif a<b:
        c = 2
    return c

def general(a, b):
    ver = verifier(a,b)
    while True:
        if ver == 0:
            print("Угадали")
            break
        elif ver == 1:
            a = int(input("Искомое число меньше. Введите число:"))
            ver = verifier(a,b)
        elif ver == 2:
            a = int(input("Искомое число больше. Введите число:"))
            ver = verifier(a,b)

def main():
    b = random.randrange(1,10)
    while True:
        a = int(input("Введите число:"))
        if a == 0:
            print("До свидания")
            break
        general(a,b)        

main()
