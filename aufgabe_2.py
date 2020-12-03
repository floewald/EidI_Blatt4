# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def intSuperliste(suplist):
    if type(suplist) == list:
        nol = 0 # number of lists
        noi = 0 # number of integer
        isIntlist = True
        for m in suplist:
            # loop to check whether al list elements are lists resp. integers
            nol += float(type(m) == list) # counts list elements
            noi += float(type(m) == int) # counts int elements

        if nol == len(suplist):
            # if all elements are lists
            # use superlist to check if it is a superlist
            for n in suplist:
                isIntlist = isIntlist and intSuperliste(n)
            return isIntlist
        elif noi == len(suplist):
            return True
        else:
            # returns false if a list is given with mixed types e.g. integer and list elements
            return False

    else:
        # return false if not a list is given
        return False

def Kopie(intListe):
    if not(intSuperliste(intListe)):
        # check if a superlist is given
        raise TypeError("Parameter is not an integer superlist! Programm terminates!")
        exit()

    # if type(intListe) != list:
    #     # returns single numbers back
    #     return intListe
    # else:
    #     copy = []
    #     for m in intListe:
    #         copy.append(Kopie(m))
    #     return copy[:]
    copy = []
    for m in intListe:
        if type(m) == int:
            return intListe[:]
        else:
            copy.append(Kopie(m))
    return copy[:]
        

L = [[1,2,3,4,5], [1], [22,4,5], [1,5]]
L = [[1], [1,2], [1]]
# L = [1]
print(intSuperliste(L))
A = [1,2]
B = [3,2]
C = [5,2,7,5]
D = [1,3,2]
L = [A, B, C, B]
print("L:\n", L)
l_copy = Kopie(L)
B.append([2,3,4])
L.append([1,2,3,4,5,6,7])
print("L:\n", L)
print("l_copy:\n", l_copy)
