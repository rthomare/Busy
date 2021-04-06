from App.models import Person
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse
import os

def home(request):
    template = loader.get_template('home/home.html')
    people = Person.objects.all().order_by('pk')
    context = {
        "people": people,
    }
    return HttpResponse(template.render(context, request))

def busy(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.busy = True
    person.save()
    return person_json_response(person)

def not_busy(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.busy = False
    person.save()
    return person_json_response(person)

def person_json_response(person):
    response = {
        'person_id': person.pk, 
        'busy': person.busy,
        'gif_url': person.image_url
    }
    return JsonResponse(response, safe=True)

