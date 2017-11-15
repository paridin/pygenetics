#UPDATE 20/01/2011
#  fix  start_population now create x,y , before x,x
#  fix  best_fitness get position of x in a population like index
#  fix  destiny - update 21 january 2011 delete *100
# fix selected the best chromosome when is size/2+1 like 51 percent  1-March-2011

__author__="Roberto Estrada"
__date__ ="Jan 13, 2011 10:09:45 AM"
import random
import os
import re
import subprocess
import sys
import time

class People:
    chromosome=[]
    fitness = 0
    id = 0

class SAT:

    #def __init__(self, path):
    def error(self,type):
        if type==100:
            print('Expect cnf value')
        elif type==110:
            print('Expect int')
        elif type==120:
            print('only one p declaration')
        elif type==130:
            print('Not expect more arguments')
        elif type==140:
            print('The character is not allowed')
        else:
            print('Error Not Found')

    def parser(self,path):
        number  = 0
        coment = '^(c)(.*)(\n)$'
        blank = '(\s*)(\n)'
        objetive_function = '^(p)\s(cnf|CNF)\s\d*\s\d*$'
        line_value = '^(((([-|~])?\d+)\s*)+)$'
        value = '^((([-|~])?\d+))$'
        file = open(path, 'r')
        ob=[]
        solution=[]
        tmp=[]
        id=0
        for line in iter(file):
            if  re.match(coment, line, re.I):
                continue
            elif re.match(blank, line, re.I):
               continue
            elif re.match(objetive_function, line, re.I):
                for char in line.split(' '):
                    if re.match('\d\n', char, re.I):
                        tmp = char.split('\n')
                        char = tmp[0]
                    if not re.match('p', char, re.I) and not re.match('cnf', char, re.I):
                        ob.append(int(char))
                        tmp=[]
            elif re.match(line_value, line, re.I):
               for char in line.split(' '):
                   if not re.match('0', char):
                       if re.match(value,  char):
                            tmp.append(int(char))
                   else:
                       solution.append( tmp)
                       id=id+1
                       tmp=[]
            else:
                print('Error file line number > {}: {}'.format(str(number), line))
                exit(-1)
            number=number+1
        file.close()
        return (ob, solution)

    def get_dir(self):
        path = os.getcwd()
        return path

    def set_clauses_in_file(self, fname):
        path = self.get_dir()+fname+'.pxm'
        fw = open(path, 'w')
        tmp=''
        cont=0
        cont1=0
        cSol=len(sol)
        for line in sol:
            for char in line:
                if(cont < len(line)-1):
                    tmp=tmp+char+' '
                    cont=cont+1
                else:
                    tmp=tmp+char
                    cont=0
            if(cont1<cSol-1):
                fw.write(tmp+'\n')
                cont1=cont1+1
            else:
                fw.write(tmp)
                cont1=0
            tmp=''
        fw.close()
        return path


class Genetic(People):
    #timers
    e_time=0.0
    i_time=0.0
    best_time=0.0
    best_chro_last_population=[]
    second=False
    def __init__(self):
        self.p=People
    def new_chromosome(self,size):
        i=0
        c=[]
        while (i<size):
            c.append(random.randint(0,1))
            i=i+1
        return c

    def start_population(self, size_row,size_col):
        i=0
        population=[]
        while (i<size_row):
            population.append(self.new_chromosome(size_col))
            i=i+1
        #DEBUG
        #for t in self.population:
        #    print t
        return population

    def new_population(self,old_population,rang,index,number_rows):
        i=0
        population=[]
        cross=[]
        cross1=[]
        mut=[]
        #print "old population: \n" + str(old_population)
        #print index[0]
        while(i<number_rows):
            desition=self.destiny(rang)
            if desition=='m':
                mut=self.mutation(old_population[index[0]])
                #print "mut chromo:"+str(mut)
                population.append(mut)
                i=i+1
            elif desition=='c':
                [cross,cross1]=self.crossover(old_population,index)
                #print "cross 0 chromo:"+str(cross)
                #print "cross 1 chromo:"+str(cross1)
                population.append(cross)
                population.append(cross1)
                i=i+2
                index[0]=random.randint(1,number_rows-1)
                index[1]=random.randint(1,number_rows-1)
        return population

    def mutation(self,population):
        #print str(population) + '<--- antes de mutar'
        size=len(population)-1
        where=random.randint(0,size)
        tmp=population[where]
        #DEBUG
        #print "Index " + str(index)
        #print "Where to mut " + str(where)
        if random.randint(1,size) > size/2+2 and self.second:
            t= True
        else:
            t= False
        if t:
            if self.best_chro_last_population[0][where] is 0:
                self.best_chro_last_population[0][where]=1
            elif tmp is 1:
                self.best_chro_last_population[0][where]=0
            return self.best_chro_last_population[0]
        else:
            if tmp is 0:
                population[where]=1
            elif tmp is 1:
                population[where]=0
            return population
        #DEBUG
        #print tmp
        #print self.population[index]
    def crossover(self,population,index):
        a=[]
        b=[]
        #print "Index: "+str(index[0])+" Index: "+str(index[1])+"\n"
        #print self.population[index[0]]
        #print self.population[index[1]]
        #print "\n"
        size = len(population[index[0]])
        #print "size: "+str(size)
        cut=random.randint(0,size)
        #print "where cut " + str(cut)+ "\n"
        i=0
        if random.randint(1,size) > size/2+1 and self.second:
            t= True
        else:
            t= False
        while(i<=size-1):
            if t:
                if i < cut:
                    a.append(self.best_chro_last_population[0][i])
                else:
                    b.append(self.best_chro_last_population[0][i])
            else:
                if i < cut:
                    a.append(population[index[0]][i])
                else:
                    b.append(population[index[0]][i])
            i=i+1
        i=0
        while(i<=size-1):
            if i >= cut:
                a.append(population[index[1]][i])
            else:
                b.append(population[index[1]][i])
            i=i+1
        #print #DEBUG
        #print "A: "+str(a)
        #print "B: "+str(b)
        #print "\n"
        return (a,b)

    def destiny(self,rang):
        #rang[0] is Mutation, rang[1] is Crossover
        dest=rang[0]
        tmp_rand=0
        tmp_rand=random.randint(0,100)
        if tmp_rand<=dest:
            return 'm'
        else:
            return 'c'

    def calculate_fitness(self,population,problem):
        z=[]
        tpos=0
        count=0

        for row in population:
            for row_ in problem:
                for pos in row_:
                    if pos<0:
                        tpos=(pos*-1)-1
                        if row[tpos]==0:
                            count=count+1
                            break
                    else:
                        tpos=pos-1
                        if row[tpos]==1:
                            count=count+1
                            break
            z.append(count)
            count=0
        return self.best_fitness(population,z)

    def qsort(self,list):
        if list==[]:
            return []
        else:
            pivot=list[0]
            lesser=self.qsort([x for x in list[1:] if x < pivot])
            greater=self.qsort([x for x in list[1:] if x >= pivot])
            return lesser + [pivot] + greater

    def best_fitness(self,population,fitness):
        pos=0
        z=self.qsort(fitness)
        #print "fit sin ordenar: " + str(fitness)
        #print "z: "+ str(z)
        for res in range(len(fitness)):
            #print "--" + str(fitness[res]) + " - " +str(res)
            if fitness[res]==z[-1]:
                pos=res
                break
        #print "position: "+str(pos)
        return self.save_best_people(population[pos],z[-1])

    def save_best_people(self,chromosome,fitness):
        #print "poblacion : " + str(self.population[position])
        #print "fitness_recibe_funcion: " + str(fitness)
        self.second=True
        self.best_chro_last_population=[]
        self.best_chro_last_population.append(chromosome)
        if self.chromosome == []:
            self.chromosome.append(chromosome)
            self.fitness=fitness
            self.best_time= time.time() - self.i_time
        else:
            if self.fitness < fitness:
                self.chromosome[0]=chromosome
                self.fitness=fitness
                self.best_time= time.time() - self.i_time
                return 'update'
        #print "chromosome: " + str( self.chromosome)
        #print "fitness: " + str(self.fitness)

"""
if __name__ == "__main__":
    pi = Genetic()
    pi.i_time = time.time()
    sat = SAT()
    #index is a variable index between 0 an size of population
    index=[]
    population=[]
    desition=''
    GENERATION = 1000
    i=0
    #rang is a variable for percent of mutation and crossover
    rang=[]

    #READ FILE
    #ob->function objetive, ob[0] is variables, ob[1] is clauses
    #sol-> problem sat,ob[x] is a clause problem, x is a index of row.
    [ob, sol] = sat.parser(sat.get_dir()+'/a2.cnf')
    #print ob
    size_row = ob[0] #kkk
    size_col = ob[0]
    #print sol
    index.append(random.randint(0,size_row-1))
    index.append(random.randint(0,size_row-1))
    #print "index : " + str(index)
    rang.append(.3) #rang[0] is mutation
    rang.append(.7) #rang[1] is crossover
    # START POPULATION RANDOM
    #print "rows: "+str(size_row) + " cols: "+str(size_col)
    population=pi.start_population(size_row,size_col) #beggin with size of variables from sat problem
    # CALCULATE FITNESS
    status=pi.calculate_fitness(population,sol)
    print "Primer calculo del fitness: " + str(pi.fitness) + "\n"
    #print population

    #print "status: "+str(status)
    #CREATE A NEW POPULATION
    old_population=population
    population=[]
    population=pi.new_population(old_population,rang,index,size_row)
    #CALCULATE FITNESS
    status=pi.calculate_fitness(population,sol)
    #print population
    #print "status: "+str(status)
    #START AG
    #print "old:  "+str(old_population)
    while(i<GENERATION):
        #print "N Generation: " + str(i) + ": "
        index[0]=random.randint(0,size_row-1)
        index[1]=random.randint(0,size_row-1)

        #CREATE NEW POPULATION
        old_population=population
        population=[]
        population=pi.new_population(old_population,rang,index,size_row)
        status=pi.calculate_fitness(population,sol)
        if status=="update":
            pi.id = i
        i=i+1

    pi.e_time = time.time()
    print '---------- RESULTADO FINAL ------------'
    print "Time: "+str(pi.e_time-pi.i_time)+" ms."
    print "Best Time "+str(pi.best_time)+" ms."
    print "Generation ID: "+str(pi.id)
    print "Number Generation: "+str(i)
    print "Best Fitness: "+str(pi.fitness)
    print "Author: " + __author__ + " Create: " +  __date__
"""

