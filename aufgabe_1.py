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

"""
recursive function but using a for loop for spacing
"""
# def pyramid(n):
#     def addSpaces(pyra, n):
#         if n == 2:
#             return "o" + pyra + "o\n"
#         else:
#             spyra = ""
#             for m in pyra.split("\n"):
#                 if not(m == ""):
#                     spyra += "o"+m+"o\n"
#             return spyra

#     if n == 1:
#         return "*"
#     else:
#         return addSpaces(pyramid(n-1),n) + pyramid(1)*(2*n-1)
    
# def pyramid_seq(n, k):
#     def insertSegment(pyra,k):
#         ipyra = ""
#         for m in pyra.split("\n"):
#             ipyra += m*k + "\n"
#         return ipyra
#     return insertSegment(pyramid(n), k)
    
def pyramid(n):
    def addSpaces(spyra):
        return "o" + "o\no".join(spyra) + "o"

    if n == 1:
        return "*"
    else:
        return addSpaces(pyramid(n-1).split("\n")) + "\n" + pyramid(1)*(2*n-1)

def pyramid_seq(n, k):
    def addlines(pyra1, pyra2, n):
        pyra = [element1 + element2 for element1, element2 in zip(pyra1, pyra2)]
        return "\n".join(pyra)
    
    if k == 1:
        return pyramid(n)
    else:
        return addlines(pyramid_seq(n, k-1).split("\n"), pyramid_seq(n, 1).split("\n"), n)

print(pyramid_seq(4,4))

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
