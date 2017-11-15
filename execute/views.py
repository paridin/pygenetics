import os
# -*- coding: utf8 -*-
#from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware.csrf import get_token
from execute.models import py_results,py_averages
#from django.utils import simplejson #deprecated
import json
from execute.pygenetics import *

def run(request):
    tuning=request.POST['tuning']
    path='/home/paridin/public_html/pyGenetics/media/cnfs/%s' % request.POST['cnffiles']
    #rang is a variable for percent of mutation and crossover
    rang=[]
    GENERATION=int(request.POST['generation'])
    type_pop = request.POST['size_population']
    rang.append(int(request.POST['mutation'])) #rang[0] is mutation
    rang.append(int(request.POST['crossover'])) #rang[1] is crossover
    nf=request.POST['cnffiles']
    pi = Genetic()
    pi.i_time = time.time()
    sat = SAT()
    #index is a variable index between 0 an size of population
    index=[]
    population=[]
    desition=''
    i=0
    #READ FILE
    #ob->function objetive, ob[0] is variables, ob[1] is clauses
    #sol-> problem sat,ob[x] is a clause problem, x is a index of row.
    [ob, sol] = sat.parser(path)
    if type_pop == 'half':
        size_row = ob[0]/2
    elif type_pop == 'double':
        size_row = ob[0]*2
    else:
        size_row = ob[0]
    size_col = ob[0]
    index.append(random.randint(0,size_row-1))
    index.append(random.randint(0,size_row-1))
    # START POPULATION RANDOM
    population=pi.start_population(size_row,size_col) #beggin with size of variables from sat problem
    # CALCULATE FITNESS
    status=pi.calculate_fitness(population,sol)
    #CREATE A NEW POPULATION
    population=pi.new_population(population,rang,index,size_row)
    #CALCULATE FITNESS
    status=pi.calculate_fitness(population,sol)
    while(i<GENERATION):
        index[0]=random.randint(0,size_row-1)
        index[1]=random.randint(0,size_row-1)
        population=pi.new_population(population,rang,index,size_row)
        status=pi.calculate_fitness(population,sol)
        if status=="update":
            pi.id = i
        i=i+1
    pi.e_time = time.time()
    try:
        u = py_results()
        result = py_results(
        user=u.get_user(2),
        time=str(pi.e_time-pi.i_time),
        best_time=str(pi.best_time),
        generation_id=pi.id,
        best_fitness=pi.fitness,
        type_tuning=tuning,
        mut_percent=rang[0],
        cross_percent=rang[1],
        num_gen=i,
        name_file=nf,)
        result.save()
    except:
        return HttpResponse('ERROR CAN NOT INSERT IN RESULTS TABLE:  '+str(result))
    result={}
    result['id']=1
    result['time']=pi.e_time-pi.i_time
    result['fitness']=pi.fitness
    return HttpResponse(json.dumps(result))
"""
def list_results(request):
    result={}
    id=0
    for i in py_results.objects.filter(user=2):
        result[id]={}
        result[id]['time'] = str(i.time)
        result[id]['best_time'] = str(i.best_time)
        result[id]['generation_id'] = i.generation_id
        result[id]['best_fitness'] = i.best_fitness
        result[id]['type_tuning'] = i.type_tuning
        result[id]['mutation_percent'] = i.mut_percent
        result[id]['crossover_percent'] = i.cross_percent
        result[id]['num_generation'] = i.num_gen
        result[id]['name_file'] = i.name_file
        id=id+1
    return HttpResponse(json.dumps(result))
"""
def list_results(request):
    from django.db import connections
    q=connection.cursor()
    result={}
    id=0
    for i in c.execute('SELECT  time_average, fitness_average, type_tuning, mut_percent, cross_percent,num_gen, av.name_file FROM execute_py_averages as av, execute_py_results as re WHERE re.name_file = av.name_file group by name_file'):
        result['id']={}
        result['id']['time_average']=i.time_average
        result['id']['fitness_average']=i.time_average
        result['id']['type_tuning']=i.type_tuning
        result['id']['mut_percent']=i.mut_percent
        result['id']['cross_percent']=i.cross_percent
        result['id']['num_gen']=i.num_gen
        result['id']['name_file']=i.name_file
        id=id+1
    return HttpResponse(json.dumps(result))

def save_log(request):
	path='/home/paridin/public_html/pyGenetics/media/logs/log_id_%s.txt' % request.POST['idlog']
	f = open(path,"w")
	for data in request.POST['log']:
		f.write(data)
	f.close()
	return HttpResponse('Save Log')

def save_averages(request):
    r=''
    try:
        r=py_averages(
        name_file=request.POST['name_file'],
        time_average=request.POST['time_average'],
        fitness_average=request.POST['fitness_average'],)
        r.save()
    except:
        return HttpResponse('ERROR CAN NOT INSERT INTO AVERAGES TABLE: '+str(r))
    return HttpResponse('DONE!!!')

