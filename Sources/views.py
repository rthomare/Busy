from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse
import os
from App.models import Person

def home(request):
    template = loader.get_template('home/home.html')
    people = Person.objects.all()
    context = {
        "people": people,
    }
    return HttpResponse(template.render(context, request))

def busy(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.busy = True
    if (request.POST.get('busy_image')):
        person.busy_image = request.POST['busy_image']
    person.save()
    template = loader.get_template('home/home.html')
    people = Person.objects.all()
    context = {
        "people": people,
    }
    return HttpResponse(template.render(context, request))

def not_busy(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.busy = False
    if (request.POST.get('not_busy_image')):
        person.not_busy_image = request.POST['not_busy_image']
    person.save()
    template = loader.get_template('home/home.html')
    people = Person.objects.all()
    context = {
        "people": people,
    }
    return HttpResponse(template.render(context, request))