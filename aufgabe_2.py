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
A = [1,2]
B = [3,2]
C = [5,2,7,5]
D = [1,3,2]
L = [A, B, C, B]
print("L:\n", L)
l_copy = Kopie(L)
L.append([1,2,3,4,5,6,7])
print("L:\n", L)
print("l_copy:\n", l_copy)