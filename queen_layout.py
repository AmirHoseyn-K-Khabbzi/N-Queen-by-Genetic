import random , time
"""

سلام استاد، من معمولا تو برنامه نویسی برا اینکه یادم نره از کجا موندم کامنت میزارم برا خودم
اینبار که کدهارو فرستادم خدمتتون کامنت هارو پاک نکردم و بهترم کردم که خودتون راحت متوجه بشید کد بر اساس
چه منطقی اجرا میشه. خیلی ممنونم

"""
#اگر بتوانم کروموزم هارا بهتر تولید کنم - ینی رندم تولید نکنم - نتیجه خیلی خوبی خواهد داد
# کروموزم ها جوری انتخاب میشوند که فقط به صورت افقی به هم گارد نگیرند
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
# عدد یک ینی برخورد و عدد صفر ینی بدون برخورد و جمعشون میکنیم
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2 
# ما هیچ برخورد عمودی نداریم - برخورد ها فقط بصورت افقی یا مورب ینی همان گوشه هستش - برخورد های افقی رو که بالا تقریبا 
# محاسبه شد به ازای هر کروموزوم
#فقط عدد صفر ینی بدون برخورد و عدد  های دیگ ینی برخورد بوده


# برخورد های مورب هم از این به بعد محاسبه شود
    diagonal_collisions = 0
    n = len(chromosome)
    left_diagonal = [0] * 2*n # برخورد های مورب سمت چپ وزیر (هم بالا هم پایین)
    right_diagonal = [0] * 2*n # برخورد های مورب سمت راست وزیر
# با استفاده از یک حلقه تعداد برخورد های هر وزیر و بصورت کروموزوم بر میگردونیم
    for i in range(n):
        # 0 +5 -1 = 4  , 4 =>2 ==> 2 + 1 = 3
        left_diagonal[i + chromosome[i] - 1] += 1 
         # 4  - 0 + 5 - 2 = 7 , 7 =>4 ==> 4 + 1 = 5
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1
    
    # print("left_diagonal: " , left_diagonal)
    # print("right_diagonal: " , right_diagonal)

# تعداد برخورد هارا بدست می اوریم -- اگر تعداد برخورد های مورب صفر باشد و همینطور تعداد برخورد های افقی هم صفر باشید
# نتیجه متد با تناسب اصلی یکی میشود
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
#مرز تایین انتقال ژن از دو والد تصادفی انتخاب شود
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
# اولین کروموزمی که درصد احتمالش بالاتر از درصد رندم باشه رو برمیگردونیم و ادامه نمیدیم
    for c, w in zip(population, probabilities):
        if upgrade + w >= r:
            return c
        upgrade += w
    assert False, "Shouldn't get here"

def generate_childe(population, fitness):
    mutation_probability = 0.03 # احتمال جهش
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) 
        y = random_pick(population, probabilities)
        child = creat_child(x, y)

        # احتمال جهش 3 درصد هستش و عدد اون هم باید رندم تولید بشه
        if random.random() < mutation_probability:
            child = Perform_the_mutate(child)
        print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population

def print_chromosome(chrom):
    print("Genetic Code = {},  Fitness = {} of {}"
        .format(str(chrom), fitness(chrom) , maxFitness))




print("PROGRAMMER: AmirHoseyn Khabbazi (sptamirhoseyn@gmail.com) "+ '\n' +" UNIVERSITY OF BONAB "+ '\n' +" Dr Hojjat Emami "+ '\n\n' +" Note that number of Queens is mean dimension of chess board ( n^n)" + '\n\n')

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
    # یک فرزند تولید میشود و به کروموزم ها اضافه میشود
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
#اول کل صفحه شطرنج خالی چیده میشه بعد وزیر ها جایگذاری می شوند
        for x in range(nq):
            board.append(["[-]"] * nq)
        for i in range(nq):
            board[nq - chrom_out[i]][i]="[Q]"
        print_chromosome(chrom)
        print_board(board)
print('\n')         
print ('...run time: %.4fs' % (time.time() - run_time))
           
            
    

