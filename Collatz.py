#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
collatz_cache = [119,125,128,144,142,137,145,171,179,174,169,182,177,177,172,\
167,180,180,175,175,157,170,183,183,209,178,191,173,173,217,186,199,168,181,\
181,194,207,238,176,238,189,189,202,215,184,184,184,197,179,210,179,179,192,\
192,192,236,205,205,218,187,187,262,187,200,169,244,182,182,182,257,195,195,\
177,208,239,208,177,221,190,252,190,190,190,234,203,203,203,216,185,247,185,\
198,260,198,198,198,185,198,242,180]

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i>0
    assert j>0
    assert i<1000000
    assert j<1000000
    v = 0
    if i==j:
        j+=1
    elif j<i:
        temp = i
        i = j
        j = temp
    assert i<j
    if (j-i > 99):
        v = collatz_eval_cache(i,j)


    else:
        for n in range(i,j):
            c = collatz_eval_helper(n)
            if c>v:
                v = c
    assert v>0
    return v

def collatz_eval_cache(i,j):
    max = 0

    a = int((i-2)/100)+1
    b = int(j/100)
    for n in range(a,b):
        t = collatz_cache[n]
        if t > max:
            max = t
        #print((n*100)+1,(n+1)*100)
    if i%100!=1:
        i2 = (a*100)
    else:
        i2 = i
    t1 = collatz_eval(i,i2)
    if t1>max:
        max = t1

    if j%100!=0:
        j2 = (b*100)+1
    else:
        j2 = j
    t2 = collatz_eval(j2,j)
    if t2>max:
        max = t2

    return max

def collatz_eval_helper(n):
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
