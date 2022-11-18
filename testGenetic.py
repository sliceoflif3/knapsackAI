from numpy.random import randint
from numpy.random import rand

W = 101
m = 2
wList = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
vList = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
cList = [1, 1, 2, 1, 2, 1, 1, 2, 2, 2]
iList = []


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


for i in range(0,len(wList)):
        iList.append(i)

        
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
            totalW += wList[cnt1]
        cnt1+=1
    #print(totalW)
    for i in range (len(x)):
        if(cList[i] not in totalC):
            totalC.append(cList[i])

    if totalW > W or len(totalC)!=m: 
        #print(totalC)
        return -1
    else:
        totalV = 0
        cnt2 = 0
        for i in x:
            if i == 1:
                totalV += vList[cnt2]
            cnt2 += 1
           
    return totalV

# initial population of random bitstring
pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
print(pop)
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

#print ([best,best_eval])

# print(pop)
# print(selected)

# print(pop)
# print(scores)
# print(best_eval)

print('Done!')
print(best)
resultList = ", ".join(map(str,best))
print(resultList)

print(type(best))
