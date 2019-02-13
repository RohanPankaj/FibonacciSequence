# Code by Craig (The best)
# Copyright © 2019, Craig A Kelley, All Rights Reserved
# Free for commercial use
# Story boarded by Sai

def fSeq(n):
    a = 0
    b = 1
    i = 0
    while not (a == n):
        i += 1
        ph = a
        a = b
        b = ph + b
        if (a > n):
            print("Error")
            break
    print(i + 1)

fSeq(int(input("Number: ")))