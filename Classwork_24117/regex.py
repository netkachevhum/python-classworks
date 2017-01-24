import re

def getar():
    f = open("1.txt",'r')
    ar = f.read().split()
    f.close()
    return ar

def normalize(ar):
    punct = "!?.,:;\'\"-—"
    arr = []
    for word in ar:
        word = word.strip("!?.,:;\«'\"-—()[»]»[1234567890").lower()
        if word != "":
            arr.append(word)
    return arr

def main(ar):
    regex = ".*[аоэиуыеёюя].*[аоэиуыеёюя].*[аоэиуыеёюя]"
    for word in ar:
        if re.search(regex,word):
            print(word)

main(normalize(getar()))
