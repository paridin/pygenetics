# Comments
# -*- coding: utf8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.middleware.csrf import get_token
from comment.models import py_comments
from django.utils import simplejson

def insert_comment(request):
    if is_ajax():
        try:
            result = py_comments(
                user=request.POST
                name=request.POST
                site=request.POST
                comment=request.POST
            )
        except:
            return HttpResponse('ERROR CAN NOT INSERT INTO COMMENT TABLE')
        return HttpResponse('Save')
    else:
        return HttpResponse('Error no XHR')

def list_comments(request):
    id=0
    data=[]
    for i in py_comments.objects.get():
        data[id]=[]
        data[id]['name'] = i.name
        data[id]['comment'] = i.comment
        data[id]['date'] = i.date
        id=id+1
    return HttpResponse(simplejson.dumps(result))

