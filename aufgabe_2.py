# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def intSuperliste(suplist):
    if type(suplist) != list:
        if type(suplist) == int:
            return True
        else:
            return False
    else:
        ini = True
        for m in suplist:
            isInt = intSuperliste(m) 
            if not(isInt):
                return False
            else:
                ini = ini and isInt
        return ini

def Kopie(intListe):
    if not(intSuperliste(intListe)):
        raise TypeError("Parameter is not an integer superlist! Programm terminates!")
        exit()
    else:
        if type(intListe) != list:
            return intListe
        else:
            copy = []
            for m in intListe:
                copy.append(Kopie(m))
            return copy

L = [[1,2,3,4,5], [22,4,5], [1,5]]
# print(intSuperliste(L))
L = [[1,2,3,4,5], [22,4,5], [1,5]]
print("L:\n", L)
l_copy = Kopie(L)
L = [[3,4,2], [2,3,4,5], [2,3,6,3]]
print("l_copy:\n", l_copy)
print("L:\n", L)