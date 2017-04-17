import os



def rmtr(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            os.remove(os.path.join(root,file))
    os.remove(folder) ##эта функция вроде бы рабочая; но на этих компьюетерах она почему-то не исполняется
    


def tree():
    for root, dirs, files in os.walk('.'):
        count = 0
        for symbol in root: #считаем, какой у нас должен быть отступ
            if symbol == '\\':
                count += 1
        proot = ''
        for i in range(0,len(root)-1): #обрезаем root, чтобы получить название текущей папки
            if root[len(root)-1-i] == '\\': #здесь можно было бы сделать сплитом, было бы гораздо быстрее
                proot = root[len(root)-i:]
                break
##        st = ''
##        for i in range(0,count):
##            st = st + '     '
##        print(st+'--'+str(proot))
            


def main1():
##    rmtr(input("enter: "))
    tree()





main1()
