#!/usr/bin/env python
from django.core.management.base import BaseCommand
from App.models import Person

class Command(BaseCommand):
    def handle(self, **options):
        # now do the things that you want with your models here
        people = Person.objects.all()
        for person in people:
            person.delete()
        rohan = Person(name="Rohan Thomare", busy=False, busy_image="https://media.giphy.com/media/g2XnJHx3LajQs/giphy.gif", not_busy_image="https://media.giphy.com/media/l2JhpjWPccQhsAMfu/giphy.gif")
        rohan.save()
        varsha = Person(name="Varsha Shenoy", busy=False, busy_image="https://media.giphy.com/media/iH6ZjzyLgZSt3j0zzG/giphy.gif", not_busy_image="https://media.giphy.com/media/2ikv7qSjhnfLxvJxCB/giphy.gif")
        varsha.save()
    