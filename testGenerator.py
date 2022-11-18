import random



def generateSmall(x):
    size = random.randint(10,40)

    randomListW = []
    randomListV = []
    randomListC = []

    m = 2 #number of class

    for i in range(0,size):
        n1 = random.randint(1,100)
        randomListW.append(n1)
        n2 = random.randint(1,100)
        randomListV.append(n2)
        n3 = random.randint(1,m)
        randomListC.append(n3)

    #W = random.randint(50,101) #weight of bag
    W = random.randint(round(sum(randomListW)/2),sum(randomListW)) #Weight equals double the average of the weight of all items to be easier to do

    with open("smallInput/INPUT_"+str(x)+".txt","w") as fp:
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

def generateLarge(x):
    size = random.randint(50,1000)

    randomListW = []
    randomListV = []
    randomListC = []

    m = random.randint(5,10)

    for i in range(0,size):
        n1 = random.randint(1,100)
        randomListW.append(n1)
        n2 = random.randint(1,100)
        randomListV.append(n2)
        n3 = random.randint(1,m)
        randomListC.append(n3)


   

    #W = random.randint(50,101) #weight of bag
    W = random.randint(round(sum(randomListW)/2),sum(randomListW)) #Weight equals double the average of the weight of all items to be easier to do

    with open("largeInput/INPUT_"+str(x)+".txt","w") as fp:
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


for i in range(1,11):
    generateSmall(i)
    generateLarge(i)