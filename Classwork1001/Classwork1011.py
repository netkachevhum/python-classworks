def getar():
    f = open("1.txt",'r')
    ar = f.read().split()
    f.close()
    return ar

def normalize(ar):
    punct = "!?.,:;\'\"-—"
    arr = []
    for word in ar:
        word = word.strip("!?.,:;\'\"-—").lower()
        if word != "":
            arr.append(word)
    return arr

def syllab(ar):
    arr = []
    voc = "аоэиуыеёюя"
    inp = int(input("Введите количество слогов:"))
    for word in ar:
        c = 0
        for letter in word:
            if letter in voc:
                c += 1
        if c == inp:
            arr.append(word)
    return arr

def first_letter(ar):
    arr = []
    inp = input("Введите первую букву:")
    for word in ar:
        if word[0] == inp:
            arr.append(word)
    return arr

def two_letters(ar):
    arr = []
    l1 = input("Введите первую букву:")
    l2 = input("Введите вторую букву:")
    for word in ar:
        ver1 = False
        ver2 = False
        for letter in word:
            if letter == l1:
                ver1 = True
            elif letter == l2:
                ver2 = True
        if ver1 and ver2:
            arr.append(word)
    return arr
    
    
def main():
    while True:
        cho = input("1 -- слова с заданным количеством слогов. \n2 -- слова, начинающиеся с заданной буквы. \n3 -- слова, содержащиеся 2 заданные буквы. \nДругой ввод -- закрыть программу. \nВведите число:")
        if cho == "1":
            print("\n".join(syllab(normalize(getar()))))
        elif cho == "2":
            print("\n".join(first_letter(normalize(getar()))))
        elif cho == "3":
            print("\n".join(two_letters(normalize(getar()))))
        else:
            print("До свидания.")
            break

if __name__ == "__main__":
    main()
