from ast import List
import random

from datetime import datetime
startTime = datetime.now()


def run(pathIn, pathOut):
    W = 0
    m = 1
    wList = []
    vList = []
    cList = []

    with open(pathIn) as f:
    #with open("smallInput/INPUT_"+str(n)+".txt") as f:
        W = int(f.readline())
        m = int(f.readline())
        wList = f.readline().split(",")
        vList = f.readline().split(",")
        cList = f.readline().split(",")
    
    a,b= local_beam_search(W,m,wList,vList,cList)

    
    with open(pathOut,"w") as fp:
        print("Writing result")
        if a == 0:
            fp.write("No solution")
        else:
            fp.write(str(a))
            fp.write("\n")
            resultList = ", ".join(map(str,b))
            fp.write(resultList)

def local_beam_search(W, n1, w, v,c):
    ''' local beam search algorithm '''
    # initialize
    n = len(w)
    best = 0
    best_x = [0] * n
    x = [0] * n
    for i in range(n):
        if random.random() < 0.5:   # random initialization
            x[i] = 1

    def evaluate(x) :
        ''' evaluate the solution '''
        total_w = 0
        total_v = 0
        total_c=[]
        for i in range(n):
            if x[i] == 1:
                total_w += int(w[i])
                total_v += int(v[i])
                if c[i] not in total_c:
                    total_c.append(c[i])
        if total_w > W or len(total_c)!=n1:    # infeasible solution
            return 0
        return total_v

    # evaluate
    best = evaluate(x)  # initial best
    best_x = x[:]   # copy
    # search
    for i in range(1000):   # 1000 iterations
        # generate a neighborhood
        neighborhood = []
        for j in range(200):    # 200 neighbors
            y = x[:]            # copy
            for k in range(n):
                if random.random() < 0.5:   # random change
                    y[k] = 1 - y[k]         # flip
            neighborhood.append(y)
        # evaluate
        for y in neighborhood:  # find the best neighbor
            z = evaluate(y)
            if z > best:
                best = z
                best_x = y[:]   # update the best solution
                x = y[:]        # update the current solution
                break           # break if a better neighbor is found

    return best, best_x


if __name__=="__main__":
    for i in range(1,11):
        pathIn = "largeInput/INPUT_" + str(i) + ".txt" 
        pathOut = "largeOutput3/OUTPUT_" + str(i) + ".txt"
        run(pathIn,pathOut)  

print(datetime.now() - startTime)