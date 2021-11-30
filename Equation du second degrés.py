#a, b, csont des valeurs toujours num�rique
from math import sqrt

def equation_second_degres (a,b,c):
    delta = b**2-4*a*c          #** au carr�
    if delta < 0:
        texte = "Cette �quation n'a pas de solution"
    elif delta == 0.0:
        sol = -b / (2*a)
        texte = "Cette �quation n'a qu'une seule solution"
    else :
        sol_1 = (-b + sqrt (delta)) / (2*a)
        sol_2 = (-b - sqrt (delta)) / (2*a)
        texte = "Cette �quation a 2 solutions possibles"
    return texte

print (str (equation_second_degres (7,9,5)))

