# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def IntegerTest(n_inp):
    try:
        n = float(n_inp)
    except ValueError:
        print("Invalid Input!")
        print("Next time use an integer...")
        exit()

    if n <= 0:
        raise ValueError("That is a negative integer!")
        print("Program terminates")
        exit()
    return n

def calcTreeHeight(h):
    if ( h > 0 ) and (h <= 11):
        return h
    elif h > 34:
        h_r1 = h - 34
        h_r2 = calcTreeHeight( (n-11)/2 )
        if (h_r1 > 0) and (h_r2 > 0):
            return float( h_r1 >= h_r2)*h_r1 + float( h_r1 < h_r2)*h_r2
        if h_r2 > 11:
            return calcTreeHeight( (h_r2 - 11)/2 )
    elif h > 11:
        return  calcTreeHeight( (n-11)/2 )
    else:
        return h
        # h = float( (h - 34) <= ( (h - 11 )/ 2 ) )*(h - 34) + float( (h - 34) > ( (h - 11 )/ 2 ) )*( (h - 11 )/ 2 )
        # h = float( (h - 34) <= ( (h - 11 )/ 2 ) )*(h - 34) + float( (h - 34) > ( (h - 11 )/ 2 ) )*( (h - 11 )/ 2 )
        # if ( (h - 34) <= 0 ) and ( (h - 34) >= calcTreeHeight( (h - 11 )/ 2 ) ):
        #     return calcTreeHeight((h - 11 )/ 2)
        # else:
        #     return calcTreeHeight(h-34)

# n_inp = input("Please Enter an integer number for the hight of the pyramid:\n")
# n = IntegerTest(n_inp)
n = 34.5
height = calcTreeHeight(n) 

print("Smalles Tree height: \t {:.5}".format(height) )