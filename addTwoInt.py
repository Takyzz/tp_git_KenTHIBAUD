#!/usr/bin/python3
import sys

def add(a, b):
    s = a + b
    return s

l=len(sys.argv)
if l == 3 :
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )

    print("Somme = ",add(a,b))

else:
    print("Erreur !! Il faut insérer 2 valeurs.")
