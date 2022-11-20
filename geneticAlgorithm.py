from numpy.random import randint
from numpy.random import rand
    

from datetime import datetime
startTime = datetime.now()


def genetic(pathIn, pathOut):
    W = 0
    m = 1
    wList = []
    vList = []
    cList = []
    iList = []

    with open(pathIn) as f:
        W = int(f.readline())
        m = int(f.readline())
        wList = f.readline().split(", ")
        vList = f.readline().split(", ")
        cList = f.readline().split(", ")


    for i in range(0,len(wList)):
        iList.append(i)
    
    # define the total iterations
    n_iter = 100
    # bits
    n_bits = len(wList)
    # define the population size
    n_pop = 100
    # crossover rate
    r_cross = 0.9
    # mutation rate
    r_mut = 1.0 / float(n_bits)

    def selection(pop, scores, k=3):
        # first random selection
        selection_ix = randint(len(pop))
        for ix in randint(0, len(pop), k-1):
            # check if better (e.g. perform a tournament)
            if scores[ix] < scores[selection_ix]:
                selection_ix = ix
        return pop[selection_ix]

    def crossover(p1, p2, r_cross):
        # children are copies of parents by default
        c1, c2 = p1.copy(), p2.copy()
        # check for recombination
        if rand() < r_cross:
            # select crossover point that is not on the end of the string
            pt = randint(1, len(p1)-2)
            # perform crossover
            c1 = p1[:pt] + p2[pt:]
            c2 = p2[:pt] + p1[pt:]
        return [c1, c2]

    def mutation(bitstring, r_mut):
        for i in range(len(bitstring)):
            # check for a mutation
            if rand() < r_mut:
                # flip the bit
                bitstring[i] = 1 - bitstring[i]


    def objective(x):
        totalW = 0
        totalC = []

        #calculate w
        cnt1 = 0
        for i in x:
            if i==1:
                totalW += int(wList[cnt1])
            cnt1+=1
        #print(totalW)
        for i in range (len(x)):
            if(cList[i] not in totalC):
                totalC.append(cList[i])

        if totalW > W or len(totalC)!=m: 
            #print(totalW)
            return -1
        else:
            totalV = 0
            cnt2 = 0
            for i in x:
                if i == 1:
                    totalV += int(vList[cnt2])
                cnt2 += 1
        return totalV


    # initial population of random bitstring
    pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
    # keep track of best solution
    best, best_eval = 0, objective(pop[0])
    # enumerate generations
    for gen in range(n_iter):
        scores = [objective(c) for c in pop]
    # check for new best solution
    for i in range(n_pop):
        # if scores[i] < best_eval:
        if scores[i] > best_eval:
            best, best_eval = pop[i], scores[i]
            print(">%d,new best f(%s) = %.3f" %(gen,pop[i],scores[i]))
    # select parents
    selected = [selection(pop,scores) for _ in range(n_pop)]
	# create the next generation
    children = list()
    for i in range(0, n_pop, 2):
        # get selected parents in pairs
        p1, p2 = selected[i], selected[i+1]
        # crossover and mutation
        for c in crossover(p1,p2, r_cross):
            # mutation
            mutation(c, r_mut)
            # store for next generation
            children.append(c)
    # replace population
    pop = children 
    
    with open(pathOut,"w") as fp:
        if best_eval != -1:
            fp.write(str(best_eval))
            fp.write("\n")
            resultList = ", ".join(map(str,best))
            fp.write(resultList)
        else:
            fp.write("No result / Can't find correct result")

if __name__=="__main__":
    for i in range(1,11):
        pathIn = "largeInput/INPUT_" + str(i) + ".txt" 
        pathOut = "largeOutput4/OUTPUT_" + str(i) + ".txt"
        genetic(pathIn,pathOut)   


print(datetime.now() - startTime)

# if __name__=="__main__":
#     for i in range(1,11):
#         pathIn = "largeInput/INPUT_" + str(i) + ".txt" 
#         pathOut = "largeOutput4/OUTPUT_" + str(i) + ".txt"
#         genetic(pathIn,pathOut)   

# if __name__=="__main__":
#     for i in range(1,2):
#         pathIn = "INPUT_test.txt" 
#         pathOut = "OUTPUT_test.txt"
#         genetic(pathIn,pathOut)  