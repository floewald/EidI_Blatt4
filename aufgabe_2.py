# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def intSuperliste(suplist):
    # if type(suplist) != list:
    #     if type(suplist) == int:
    #         return True
    #     else:
    #         return False
    # else:
    #     ini = True
    #     for m in suplist:
    #         isInt = intSuperliste(m)
    #         if not(isInt):
    #             return False
    #         else:
    #             ini = ini and isInt
    #     return ini
    if type(suplist) == list:
        nol = 0 # number of lists
        noi = 0 # number of integer
        isIntlist = True
        for m in suplist:
            nol += float(type(m) == list)
            noi += float(type(m) == int)

        if nol == len(suplist):
            for n in suplist:
                isIntlist = isIntlist and intSuperliste(n)
            return isIntlist
        elif noi == len(suplist):
            return True
        else:
            return False

    else:
        return False

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

L = [[1,2,3,4,5], [1], [22,4,5], [1,5]]
L = [[1], [1,2], [1]]
# L = [1]
print(intSuperliste(L))
# A = [1,2]
# B = [3,2]
# C = [5,2,7,5]
# D = [1,3,2]
# L = [A, B, C, B]
# print("L:\n", L)
# l_copy = Kopie(L)
# B.append([2,3,4])
# # L.append([1,2,3,4,5,6,7])
# print("L:\n", L)
# print("l_copy:\n", l_copy)