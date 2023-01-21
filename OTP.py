#!/usr/bin/python3
import random
import sys

random.seed(int(input("Enter the seed: ")))
ed = input("Enter e to encrypt or d to decrypt: ")
if ed=="e":
    plain=bytes(input("Enter the text: "),"UTF-8")
    lp=len(plain)
    key=random.randbytes(lp)
    lpmo=lp-1
    for i,c in enumerate(plain):
        sys.stdout.write(str(plain[i]^key[i])+("," if i<lpmo else ""))
elif ed=="d":
    allnumbers = input("Enter the numbers: ").split(",")
    key=random.randbytes(len(allnumbers))
    for i,s in enumerate(allnumbers):
        allnumbers[i]=int(s)^key[i]
    print(bytes(allnumbers).decode("UTF-8"))
else:
    print("Unrecognized option.")
