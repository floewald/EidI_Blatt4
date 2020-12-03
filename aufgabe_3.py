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
    if h > 34:
        h1 = calcTreeHeight(h-34)
        h2 = calcTreeHeight((h-11)/2)
        return float(h1<h2)*h1 + float(h1>h2)*h2
    elif h > 11:
        return calcTreeHeight((h-11)/2)
    else:
        return h

n_inp = input("Please Enter an integer number for the hight of the pyramid:\n")
n = IntegerTest(n_inp)
height = calcTreeHeight(n) 

print("Smalles Tree height: \t {:.5}".format(height) )