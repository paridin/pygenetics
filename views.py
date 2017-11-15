import os.path
# -*- coding: utf8 -*-
# from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware.csrf import get_token
from django.views.decorators.http import condition

def index(request):
    #header
    title='Sintonización de un Algoritmo Genético para la resolución de problemas SAT. '
    es_mx="Español"
    en_usa="Ingles"
    #form labels
    upload_label='Seleccionar un archivo CNF '
    button_upload='Cargar Archivo'
    file_desc='Archivos: '
    or_label='ó'
    file_selected="El archivo seleccionado es: "
    list_label='Listar Archivos'
    page_label='Páginas: '
    m_label='Mutación: '
    c_label='Cruzamiento: '
    size_population_label='Tamaño de la población: '
    op_half='Mitad'
    op_normal='Normal'
    op_double='Doble'
    g_label='Número de Generaciones: '
    t_label='Selecciona el tipo de sintonización: '
    op_select='Seleccionar'
    op_mut_cross='Mutación y Cruzamiento'
    op_size_population='Tamaño de Población'
    op_size_generation='Número de Generaciones'
    j_label='Enviar Trabajo'
    l_job = 'Trabajo # '
    #comments labels
    leave_a_comment='Deja un comentario'
    c_name='Nombre: '
    c_email='Correo Electronico: '
    c_web='Sitio Web: '
    c_press='Comentar'
    # ERRORS MESSSAGES
    ERROR_INT='No es un número'
    ERROR_SIZE='El número no puede ser mayor a 100%'
    ERROR_NOT_CNF='No es un archivo CNF'
    ERROR_EMPTY='Existen uno o más campos vacíos'
    #section status labels
    sub_title_status='Instrucciones'
    desc_content='Rellena los campos con los datos que creas pertinentes, envia tu trabajo presionando el botón de correr'
    #footer
    build_by='Desarrollado por'
    build_name='Paridin Company'
    return render_to_response('index.html', locals())

def index_us(request):
    #header
    title='Tuning Genetic Algorithm to solve SAT problems. '
    es_mx="Spanish"
    en_usa="English"
    #form labels
    upload_label='Choose file CNF '
    button_upload='Upload File'
    file_desc='Files: '
    or_label='or'
    file_selected="The selected file is: "
    list_label="List files"
    page_label='Pages: '
    m_label='Mutation: '
    c_label='Crossover: '
    size_population_label='Size of Population: '
    op_half='Half'
    op_normal='Normal'
    op_double='Double'
    g_label='Number of Generations: '
    t_label='Select type of tunning: '
    op_select='Select'
    op_mut_cross='Mutation and crossover'
    op_size_population='Size of Population'
    op_size_generation='Number of Generations'
    j_label='Submit Job'
    l_job= 'Job # '
    #comments labels
    leave_a_comment='Leave a comment'
    c_name='Name: '
    c_email='Email: '
    c_web='Web Page: '
    c_press='Comment'
    # ERRORS MESSSAGES
    ERROR_INT='Is not a number'
    ERROR_SIZE='The number cannot be greater than 100%'
    ERROR_NOT_CNF='Is not a CNF file'
    ERROR_EMPTY='Exist one or more fields empty'
    #section status labels
    sub_title_status='Instructions'
    desc_content='Fill the fields with pertinent data, after, press the button "Submit Job" to send your job.'
    #footer
    build_by='Developed by'
    build_name='Paridin Company'
    return render_to_response('index.html',locals())

def upload(request):
    #if request.is_ajax():
    path = '/home/paridin/public_html/pyGenetics/media/cnfs/%s' % request.FILES['cnffile'].name
    f = request.FILES['cnffile']
    try:
        destination = open(path, 'wb+')
    except:
        return HttpResponse("Error to open check permissions " + path)
    try:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    except:
        return HttpResponse("Error to write in a disk " + path)
    return HttpResponse("Success upload " + path)
    #else:
    #    return HttpResponse('Error no XHR')

def get_cnf(request):
    return HttpResponse(cnf2html(request.POST['id']), mimetype='text/html')

def cnf2html(id):
    # 2E9AFE  - blue , FE2E2E - red, 848484 -gray
    import re
    path = '/home/paridin/public_html/pyGenetics/media/cnfs/%s' % id
    html=""
    coment = '^(c)(.*)(\n)$'
    blank = '(\s*)(\n)'
    objetive_function = '^(p)\s(cnf|CNF)\s\d*\s\d*$'
    line_value = '^(((([-|~])?\d+)\s*)+)$'
    file = open(path, 'r')
    html+= "<div>"
    for line in iter(file):
        if  re.match(coment, line, re.I):
            html+= "<p style='color:#2E9AFE;margin:0;padding:0;''>%s</p>" % line
        elif re.match(blank, line, re.I):
            continue
        elif re.match(objetive_function, line, re.I):
            html+= "<p style='color:#FE2E2E'>%s</p>" % line
        elif re.match(line_value, line, re.I):
            html+= "<p style='color:#848484;margin:0;padding:0;'>%s</p>" % line
    html+= "</div>"
    return html

def upload_progress(request):
    from django.utils import simplejson
    cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], request.GET['X-Progress-ID'])
    data = cache.get(cache_key)
    return HttpResponse(simplejson.dumps(data))

def list_cnf(request):
    from django.utils import simplejson
    if request.is_ajax():
        files=[]
        result={}
        id=0
        path='/home/paridin/public_html/pyGenetics/media/cnfs/'
        files.append([file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))])
        for i in range(len(files[0])):
            result[i]=files[0][i]
        return HttpResponse(simplejson.dumps(result))
    else:
        return HttpResponse('Error no XHR')

def test(request):
    return render_to_response('test.html',locals())

