import os

def create_folders():
    #просто создаем вложенные друг в друга папки
    path = str(input("Введите предложение:")).replace(" ","/")
    os.makedirs(path)

def create_folders_bynum():
    n = int(input("Enter a number "))
    for i in range(1,n+1):
        os.mkdir(str(i))
        for y in range(1,i+1):
            f = open(str(i)+"/"+str(y)+".txt","w")


def only_folders():
    files = os.listdir(".")
    print(files)
    for file in files:
        if os.path.isdir(file):
            print(file)
        
        

only_folders()
