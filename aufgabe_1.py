# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def IntegerTest(n_inp):
    try:
        n = int(n_inp)
    except ValueError:
        print("Invalid Input!")
        print("Next time use an integer...")
        exit()

    if n <= 0:
        raise ValueError("That is a negative integer!")
        print("Program terminates")
        exit()
    return n

def pyramid(n):
    if n == 1:
        return "*"
    else:
        pyralist = pyramid(n-1).split("\n")
        pyra = "o" + "o\no".join(pyralist) + "o"
        return pyra + "\n" + pyramid(1)*(2*n-1)

def pyramid_seq(n, k):
    if k == 1:
        return pyramid(n)
    else:
        pyra1 = pyramid_seq(n, 1).split("\n")
        pyra2 = pyramid_seq(n, k-1).split("\n")
        pyra = [element1 + element2 for element1, element2 in zip(pyra1, pyra2)]
        return "\n".join(pyra)

n_inp = input("Please Enter an integer number for the hight of the pyramid:\n")
n = IntegerTest(n_inp)

print("#"*15)
print(pyramid(n))
print("#"*15)


n_inp = input("Please Enter an integer number for the hight of the pyramid:\n")
n = IntegerTest(n_inp)
k_inp = input("Please Enter an integer number for the number of times of the pyramid:\n")
k = IntegerTest(k_inp)


print("#"*15)
print(pyramid_seq(n,k))
print("#"*15)