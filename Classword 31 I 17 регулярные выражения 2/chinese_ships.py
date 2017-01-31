import re

def getar():
    f = open("china.txt",'r',encoding="utf8")
    ar = f.read()
    f.close()
    return ar

##def normalize(ar):
##    punct = "!?.,:;\'\"-—"
##    arr = []
##    for word in ar:
##        word = word.strip("!?.,:;\«»'\"|…-—()][*1234567890").lower()
##        if word != "":
##            arr.append(word)
##    return arr


def find_names(ar):
    reg = "«(?:[а-яА-Я ]+?-[123456789])|(?:Юйту)»" #программа не доделана. getar работает так, как надо, но название возвращаемого файла с ним
    values = re.findall(reg,ar)                 #никак не соотносится

    print(values)
    

find_names(getar())

#print("\n".join(normalize(getar())))
