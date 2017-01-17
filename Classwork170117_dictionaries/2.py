def open_file():
    f = open("1.txt",'r')
    ar = f.read().split()
    arr = []
    for word in ar:
        if not word.strip('!?.,):;\'(\"-—') == "":
            arr.append(word.strip('!?.,):;\'(\…"-—').lower())
    return arr

def freq(ar):
    wordc = {}
    for word in ar:
        if word not in wordc:
            wordc[word] = 1
        else:
            wordc[word] += 1
    return wordc

def outp(d):
    for key in d:
        print(key+" - "+str(d[key]))

outp(freq(open_file()))
        
