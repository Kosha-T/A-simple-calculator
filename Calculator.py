import math
from math import sqrt

def affich(text):
    print()
    print(text)


def saisie_calc():
    calc = input("Voici les opérateurs proposés\n [nombre1] + [nombre2] >< Addition\n [nombre1] - [nombre2] >< Soustraction\n [nombre1] * [nombre2] >< Multiplication\n [nombre1] / [nombre2] >< Division\n")
    splitCalc = calc.split()

    if splitCalc[1] == "+":
        the_result = (float(splitCalc[0]) + float(splitCalc[2])) 
        affich(the_result)

    elif splitCalc[1] == "-":
        the_result = float(splitCalc[0]) - float(splitCalc[2]) # on soustrait l'arg 0 par l'arg 1 (ce sont les nombres)
        affich(the_result)

    elif splitCalc[1] == "*":
        the_result = float(splitCalc[0]) * float(splitCalc[2]) # on multiplie l'arg 0  par l'arg 1 (ce sont les nombres)       
        affich(the_result)

    elif splitCalc[1] == "/":
        the_result = float(splitCalc[0]) / float(splitCalc[2]) # on divise l'arg 0 par l'arg 1  (ce sont les nombres) 
        affich(the_result) 
saisie_calc()