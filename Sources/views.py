from App.models import Person
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse
import os

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
    person.save()
    return JsonResponse(person, safe=False)

def not_busy(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.busy = False
    person.save()
    return JsonResponse(person, safe=False)
