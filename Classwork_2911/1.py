



def main():
    f = open("1.txt",'r')
    #l = 0
    for line in f:
        w = line.split()
        for word in w:
            if word[0] in "ауоыиэяюёе":
                print(word)
    #print(l)


if __name__ == '__main__':
    main()
