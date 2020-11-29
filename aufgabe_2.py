# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def intSuperliste(suplist):
    if type(suplist) != int:
        if type(suplist) == int:
            return True
        else:
            return False
    else:
        return intSuperliste(suplist)

L = [[1,2,3,4,5], ["f",4,5], ["f", "5"]]

# print(intSuperliste(L))
n = -1
if type(n)!=int:
    raise TypeError("Not an Integer")
if n<0:
    raise ValueError("Must be positiv")
