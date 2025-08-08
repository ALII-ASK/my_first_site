from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render

def members(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context , request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template=loader.get_template('details.html')
    contex={
        'mymember':mymember,
    }
    return HttpResponse(template.render(contex , request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template("template.html")
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

    