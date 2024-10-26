def otodik():
    n = 0
    #első megoldás
    for n in range(60, -70, -1):
        print(str(n)+",", end=" ")
    print("-70")

    #masodik megoldás
    for n in range(60, -70-1, -1):
        print(","+str(n), end=" ")