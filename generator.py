from itertools import permutations
import timeit

def gen(n):
    One=[]
    c=0
    while n>=c:
        g=str(c)+str(c)
        One.append(str(g))
        f=str(c)+'p'
        One.append(str(f))
        c=c+1
    One.remove('0p')
    return One

def all_diags(n):
    s=timeit.default_timer()
    lst = gen(n)
    perm = permutations(lst)
    hmm=[]
    for i in list(perm):
        hmm.append(i)
    fin=[]
    for i in hmm:
        c=-1
        tmp2=[]
        for k in gen(n):
            c=c+1
            tmp=[]
            tmp.append(k)
            tmp.append(i[c])
            tmp2.append(tmp)
        fin.append(tmp2)
    st=timeit.default_timer()
    print('Time Generator:',st-s)
    return fin

def genny(n):
    G=(2*n)+1
    One=[]
    c=0
    while n>=c:
        g=str(c)+str(c)
        One.append(str(g))
        f=str(c)+'p'
        One.append(str(f))
        c=c+1
    One.remove('0p')
    One.remove('00')
    chunkii=[]
    for x in range(0, len(One), 2):
        chunkii.append(One[x:x+2])
    return chunkii