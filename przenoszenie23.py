import shutil
import os
destination = "D:/Nauka/SADSA/Lublinwies/pozioma/" #sciezka gdzie bede wrzucal
destination2 = "D:/Nauka/SADSA/Lublinwies/pozioma" #sciezka gdzie bede wrzucal
source = os.listdir(destination2) #lista dla folderu aaa
nowa=[]
for g in source:
    nowa.append(g[0:4]) #przepisuje sobie do nowej listy tylko poczatki pliczkow
count = list(set(nowa))#Funkcja set tworzy kolekcj? uporz?dkowanych i unikalnych element?w. Natomiast funkcja list zamienia kolekcj? w list?. W wyniku otrzymujemy uporz?dkowan? list? z usuni?tymi duplikatami.


for files in source: #dla plikow w liscie
    for c in count:
        if files.startswith(c) and os.path.isfile(destination+files): # jezeli plik nazywa sie 4 pierwsze i jest plikiem to
            if not os.path.exists(destination+files[0:4]): os.makedirs(destination+files[0:4])# jezeli folder nie istnieje to stworz taki
            shutil.copy("D:/Nauka/SADSA/Lublinwies/pozioma/"+files,destination+files[0:4]) # kopiuj z sciezka+nazwapliku do destination o nazwie pierwsze cztery
#jezeli dany plik juz jest w miejscu docelowym to sie wykrzaczy :)