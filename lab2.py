import numpy as np
Wierz = ['A',
         'B',
         'C',
         'D',
         'E',
         'F',
         'G']
graph = {'A': ['C', 'D'],
         'B': ['C', 'F'],
         'C': ['A', 'E', 'D', 'B'],
         'D': ['A', 'C', 'G'],
         'E': ['C', 'F'],
         'F': ['B', 'E', 'G'],
         'G': ['D', 'F']
         }
kosztA = [1, 2]
kosztB = [2, 3]
kosztC = [1, 3, 1, 2]
kosztD = [2, 1, 1]
kosztE = [3, 2]
kosztF = [3, 2, 1]
kosztG = [1, 1]
class krawedz:
    def __init__(self):
        self.poczatek = ' '
        self.koniec = ' '
        self. koszt = 0
krawedzie = []
ile = 0
for i in range(kosztA.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i].poczatek = 'A'
    krawedzie[i].koniec = graph['A'][i]
    krawedzie[i].koszt = kosztA[i]
ile = ile + kosztA.__len__()
for i in range(kosztB.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i + ile].poczatek = 'B'
    krawedzie[i + ile].koniec = graph['B'][i]
    krawedzie[i + ile].koszt = kosztB[i]
ile = ile + kosztB.__len__()
for i in range(kosztC.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i + ile].poczatek = 'C'
    krawedzie[i + ile].koniec = graph['C'][i]
    krawedzie[i + ile].koszt = kosztC[i]
ile = ile + kosztC.__len__()
for i in range(kosztD.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i + ile].poczatek = 'D'
    krawedzie[i + ile].koniec = graph['D'][i]
    krawedzie[i + ile].koszt = kosztD[i]
ile = ile + kosztD.__len__()
for i in range(kosztE.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i + ile].poczatek = 'E'
    krawedzie[i + ile].koniec = graph['E'][i]
    krawedzie[i + ile].koszt = kosztE[i]
ile = ile + kosztE.__len__()
for i in range(kosztF.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i + ile].poczatek = 'F'
    krawedzie[i + ile].koniec = graph['F'][i]
    krawedzie[i + ile].koszt = kosztF[i]
ile = ile + kosztF.__len__()
for i in range(kosztG.__len__()):
    krawedzie.append(krawedz())
    krawedzie[i + ile].poczatek = 'G'
    krawedzie[i + ile].koniec = graph['G'][i]
    krawedzie[i + ile].koszt = kosztG[i]

def dikstry(pocz, kon):
    Q = [    'A',
             'B',
             'C',
             'D',
             'E',
             'F',
             'G']
    S = []

    slow = {'A': 0,
         'B': 1,
         'C': 2,
         'D': 3,
         'E': 4,
         'F': 5,
         'G': 6
         }
    d = []
    for i in range(Q.__len__()):
        d.append(np.infty)
    p = []
    for i in range(Q.__len__()):
        p.append('X')
    d[slow[pocz]] = 0
    while Q != []:
        temp = []
        for i in Q:
            temp.append(d[slow[i]])
        mini = np.argmin(temp)
        for i in range(7):
            if Q[mini] == Wierz[i]:
                argmini = i

        S.append(Wierz[argmini])
        Q.remove(Wierz[argmini])
        for i in krawedzie:
            if i.poczatek == Wierz[argmini]:
                if d[slow[i.koniec]] > i.koszt + d[argmini]:
                    d[slow[i.koniec]] = i.koszt + d[argmini]
                    p[slow[i.koniec]] = Wierz[argmini]
    # print(p)
    # print(d)
    droga = []
    koniec = False
    kierunek = slow[kon]
    droga.append(kon)
    while koniec == False:
        if p[kierunek] != 'X':
            droga.append(p[kierunek])
            kierunek = slow[p[kierunek]]
        else:

            koniec = True
    print("Koszt " + str(d[slow[kon]]))
    print("Droga: " + str(droga[::-1]))
dikstry('E','D')
