##программа получает слово и определяет, к какому склонению оно относится

word = input("Enter a word:")
c = False
endings = ['о','е','а','я','у','ю','ом','ем']


for i in range(0,len(endings)):
    if word.endswith(endings[i]):
        print("Принадлежит 2 скл.")
        c = True
        break

if not c:
    print("Не принадлежит 2 скл")
        

    
