##сегодня пишем шифровальные прораммы. Все программы работают в цикле. Разные способы шифрования.

##def inp():
##    a = input("Enter smth:")
##    if a == "":
##        return ""

#def repl()



#программа сейчас не совсем в рабочем виде. Я хотел сделать дешифрацию и шифровку
#опцией одной программы. Для этого: сперва сделать так, чтобы, подходя к последним двум
#элементам, программа автоматически переходила на первый; сложность в том, что нельзя просто ограничить ищейку по алфавиту.
#нужны, похоже, две переменные. Возомжно, придется все сделать заново
def ch(a):
    alph = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    ar = ""
    for q in range(len(a)):
        ver = True
        q3 = 0
        for q2 in range(len(alph)):
            if q2 == len(alph)-2:
                q3 = 0
            elif q2 == len(alph)-1:
                q3 = 1
            else:
                q3 = q2

            if a[q] == alph[q2]:
                ar = ar + alph[q2+2]
                ver = False
                break
        if ver:
            ar = ar + a[q]
    print(ar)
    
def main():
    while True:
        a = input("enter string")
        if not a == "":
            ch(a)
        else:
            print("Null input")
            break
    
main()
