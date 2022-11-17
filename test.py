W = 101
m = 2
randomListW = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
randomListV = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
randomListC = [1, 1, 2, 1, 2, 1, 1, 2, 2, 2]

with open("INPUT_test.txt","w") as fp:
    fp.write(str(W)+"\n")
    fp.write(str(m)+"\n")
    randomListW2 = ', '.join(map(str,randomListW))
    fp.write(randomListW2)
    fp.write("\n")
    randomListV2 = ', '.join(map(str,randomListV))
    fp.write(randomListV2)
    fp.write("\n")
    randomListC2 = ', '.join(map(str,randomListC))
    fp.write(randomListC2)

fp.close()