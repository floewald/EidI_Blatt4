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

L = [[1,2,3,4,5], [22,4,5], [1,5]]

print(intSuperliste(L))
