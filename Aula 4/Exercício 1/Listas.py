import random

L = [random.randint(0, 100) for x in range(random.randint(10, 100))]

for x in L:
    if x % 2 == 0:
        print (str(x).strip('[]'), " - True")
    else:
        print (str(x).strip('[]'), " - False")
