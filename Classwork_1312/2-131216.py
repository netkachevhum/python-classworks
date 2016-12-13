

def words(name):
    f = open(name,'r')
    words = f.read().split()
    f.close()
    for i,word in enumerate(words):
        words[i] = word.strip('\'\".,!?:;`()\\n').lower()
    return(words)


print(words('1.txt'))
