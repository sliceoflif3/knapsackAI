from itertools import combinations

from datetime import datetime
startTime = datetime.now()

    
def bruteForceKnapsack(pathIn, pathOut):
    W = 0
    m = 1
    wList = []
    vList = []
    cList = []
    iList = []

    with open(pathIn) as f:
    #with open("smallInput/INPUT_"+str(n)+".txt") as f:
        W = int(f.readline())
        m = int(f.readline())
        wList = f.readline().split(", ")
        vList = f.readline().split(", ")
        cList = f.readline().split(", ")

    for i in range(0,len(wList)):
        iList.append(i)


    subsets = []

    for i in range(len(iList)+1):
        subsets += [list(j) for j in combinations(iList,i)]

    legalSubset = []

    run = 0

    for subset in subsets:
        print(run)
        run += 1
        totalW = 0
        totalC = []
        for i in subset:
            totalW += int(wList[i])
            if (cList[i] not in totalC):
                totalC.append(cList[i])
        if totalW <= W and len(totalC)==m:
            legalSubset.append(subset)

    # print(legalSubset)

    maxVIndex = -1
    maxV = -1
    for subset in legalSubset:
        totalV = 0
        for i in subset:
            totalV += int(vList[i])
        if totalV > maxV:
            maxV = totalV
            maxVIndex = subsets.index(subset)

    result = []
    for i in range(0,len(wList)):
        result.append(0)

    for i in subsets[maxVIndex]:
        result[i]=1

    with open(pathOut,"w") as fp:
        print("Writing result")
        if maxV == -1:
            fp.write("No solution")
        else:
            fp.write(str(maxV))
            fp.write("\n")
            resultList = ", ".join(map(str,result))
            fp.write(resultList)


for i in range(1,6):
    pathIn = "smallInput/INPUT_" + str(i) + ".txt" 
    pathOut = "smallOutput/OUTPUT_" + str(i) + ".txt"
    bruteForceKnapsack(pathIn,pathOut)   

# for i in range(1,6):
#     pathIn = "largeInput/INPUT_" + str(i) + ".txt" 
#     pathOut = "largeOutput/OUTPUT_" + str(i) + ".txt"
#     bruteForceKnapsack(pathIn,pathOut)   


print(datetime.now() - startTime)