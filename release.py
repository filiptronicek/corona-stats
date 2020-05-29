def newRls():
    with open("rls.txt", "r") as f:
        lines = f.readlines()

    vrsTxt = lines[-1].split(".")

    if int(vrsTxt[-1]) < 9:
        vrsTxt[-1] = int(vrsTxt[-1]) + 1
    elif int(vrsTxt[1]) < 9:
        vrsTxt[1] = int(vrsTxt[1]) + 1
        vrsTxt[-1] = 0

    else:
        vrsTxt[0] = int(vrsTxt[0]) + 1
        vrsTxt[-1] = 0
        vrsTxt[-2] = 0
    with open("rls.txt", "w") as f:
        f.write(str(vrsTxt[0])+"."+str(vrsTxt[-2])+"."+str(vrsTxt[-1]))
    with open("rls.txt", "r") as f:
        linesNw = f.readlines()[0]

    return linesNw
print(newRls())