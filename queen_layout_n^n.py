import random , time

def create_random_chromosome(size): 
    a = []
    ran = 0
    counter = 0
    for _ in range(nq):
        ran = random.randint(1, nq)
        # print("main ran: " ,ran)
        if counter == 0:
            # print('first set')
            a.append(ran)
        
        elif counter != 0:
            # print("counter: " , counter )
            while 1 == 1:
                if ran in a:
                    # print("not match :" , ran  , " => ran list: " , a)
                    ran = random.randint(1, nq)
                    # print("new ran: " , ran)
                    continue
                else:
                    # print("ok: " , ran)
                    a.append(ran)
                    break

        counter += 1  
    print("#" , end='')
    return a


#------------------------------------------------------------------------------------------------------------------------------------------------
def fitness(chromosome): 
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2 


    diagonal_collisions = 0
    n = len(chromosome)
    left_diagonal = [0] * 2*n 
    right_diagonal = [0] * 2*n 
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1 
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1
    
    # print("left_diagonal: " , left_diagonal)
    # print("right_diagonal: " , right_diagonal)

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
    # print("diagonal_collisions: " , diagonal_collisions)
    #28-(2+3)=23
    return int(maxFitness - (horizontal_collisions + diagonal_collisions)) 

#-----------------------------------------------------------------------------------------------------------------------------------


def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

        
def creat_child(x, y): 
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def Perform_the_mutate(x): 
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    # print("r: " , r)
    # print("total: " , total)
    upgrade = 0
    for c, w in zip(population, probabilities):
        if upgrade + w >= r:
            return c
        upgrade += w
    assert False, "Shouldn't get here"

def generate_childe(population, fitness):
    mutation_probability = 0.03 
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) 
        y = random_pick(population, probabilities)
        child = creat_child(x, y)

        if random.random() < mutation_probability:
            child = Perform_the_mutate(child)
        print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population

def print_chromosome(chrom):
    print("Genetic Code = {},  Fitness = {} of {}"
        .format(str(chrom), fitness(chrom) , maxFitness))




print("PROGRAMMER: AmirHoseyn Khabbazi (sptamirhoseyn@gmail.com) "+ '\n\n' +" Note that number of Queens is mean dimension of chess board ( n^n)" + '\n\n')

print("If there is any problem just let me know to explain, thanks..." + '\n\n')


nq = int(input(">> PLZ Enter your queens number: ")) # 8
run_time = time.time()

if(nq < 4):
    print("queen number must be bigger than 3, not even 3" + '\n' + "please re-run the app")
    exit()

maxFitness = (nq*(nq-1))/2  # 8*7/2 = 28 
print("Creating chromosomes... , please wait (" , end='')
chrom_population = [create_random_chromosome(nq) for _ in range(100)]
print(") 100%" +'\n' + "Create chromosomes is done")
# print(chrom_population)
# print(type(chrom_population))
# chrom_population = list(dict.fromkeys(chrom_population))
generation = 1
counn = 0
while not maxFitness in [fitness(chrom) for chrom in chrom_population]: 
    print("=== Generation {} ===".format(generation))
    chrom_population = generate_childe(chrom_population, fitness)
    print("")
    print("Maximum Fitness of this Generation= {} of {}".format(max([fitness(n) for n in chrom_population] ) , maxFitness))
    generation += 1
    counn +=1
    if counn == 30:
        counn = 0
        print("Creating new chromosomes population... , please wait (" , end='')
        chrom_population = [create_random_chromosome(nq) for _ in range(100)]
        print(") 100%" +'\n' + "Create chromosomes is done")

chrom_out = []


def print_board(board):
    for row in board:
        print (" ".join(row))

print("Solved in Generation {}!".format(generation-1))
for chrom in chrom_population:
    if fitness(chrom) == maxFitness:
        board = []
        print("")
        print("solution found: ")
        chrom_out = chrom
        for x in range(nq):
            board.append(["[-]"] * nq)
        for i in range(nq):
            board[nq - chrom_out[i]][i]="[Q]"
        print_chromosome(chrom)
        print_board(board)
print('\n')         
print ('...run time: %.4fs' % (time.time() - run_time))
           
            
    

