import numpy as np
import time
import random as r

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

tab = []
ile = 5000
for i in range (ile):
    tab.append(r.randint(1,ile))

tab2 = []
for i in tab:
    tab2.append(i)

tab3 = []
for i in tab:
    tab3.append(i)

@timing
def babelkowe(tab, ile):
    koniec = False
    while koniec == False:
        for i in range(ile):
            if i==0:
                koniec = True
            if i != ile - 1 and tab[i] > tab[i+1]:
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
                koniec = False
@timing
def wymiana(tab, ile):
    posortowane = []
    for i in range(ile):
        min = ile
        for j in range(ile-i):
            if min > tab[j]:
                min = tab[j]
        tab.remove(min)
        posortowane.append(min)
    return posortowane
@timing
def do_quick(tab, ile):
    quick(tab, 0, ile - 1)

def quick(tab, lewy, prawy):
    i = int((lewy + prawy)/2)
    piwot = tab[i]
    tab[i] = tab[prawy]
    j = lewy
    for i1 in range(lewy, prawy ):
        if tab[i1] < piwot:
            temp = tab[j]
            tab[j] = tab[i1]
            tab[i1] = temp
            j = j + 1
    tab[prawy] = tab[j]
    tab[j] = piwot
    if lewy < j - 1:
        quick(tab, lewy, j-1)
    if j + 1 < prawy :
        quick(tab, j + 1, prawy)


if tab3 == tab and tab == tab2:
    print("ok")
babelkowe(tab3,ile)
do_quick(tab,ile)
sort = wymiana(tab2,ile)
if sort == tab and tab == tab3:
    print("ok")



