import xlwt
import os

plik = open('juzek1.txt','r')
lista = []
calosc = ""
wb = xlwt.Workbook(encoding='utf-8')
#ws = wb.add_sheet('Sheet')
ws = wb.add_sheet('Sheet', cell_overwrite_ok=True)
w = 1
k = 1 # wspolrzedne poczatku
n = 1 # zliczacz do braku srednika
g = 0 # zliczam koncowki
s=1
zlicz =""
try:
        for i in plik:
            i = i.strip('\n')
            b = i.split(':')
            s = s+1
            #calosc = calosc + i + ';'
            #g = 1+g
            if i != "":
                if i[0:71] == "======================================================================:":
                    if g> 120:
                        ws = wb.add_sheet('Sheet%d'% (s), cell_overwrite_ok=True)
                        g = 0
                        k = 1
                        w = 1
                    else:
                        k = k+2 #jezeli krecha to do nowej kolumny
                        w = 1
                        g = g +1

                else:
                        if i.find(":") == -1:#jezeli nie ma srednika:
                                #ws.write(w, k, b[0]) # zapis do komorki
                                if n<2:
                                    calosc = zlicz + b[0].strip()
                                    ws.write(w-1,k+1, calosc)
                                else:
                                    calosc = calosc +b[0].strip()
                                    ws.write(w-1,k+1, calosc)
                                n=n+1
                                #w = w + 1
                                #if g%2 == 1:
                                #        ws.write(w-1, k,zlicz[1] +" "+ b[0]) # zapis do komorki
                                #else:
                                #        ws.write(w-1,k,zlicz[0] +b[0])
                                #w = w + 1
                        else: #jezeli jest srednik:
                                ws.write(w, k, b[0])
                                ws.write(w,k+1,b[1].strip()) #ucinam puste pola  x % 2 and 'nieparzysta' or 'parzysta'
                                calosc=""
                                n=1
                                zlicz=b[1].strip()
                                w = w + 1 # zrob tu zapisanie, i zeruj zliczacz, zliczacz wrzuc do tego wyzej

finally:
	plik.close()

wb.save('juzek1.xls')
#wb2 = xlrd.open_workbook()
#ws2 =wb2.sheet_by_name('Sheet')
#;C:\Program Files (x86)\HOTOSM\python\2.5\site-packages;
