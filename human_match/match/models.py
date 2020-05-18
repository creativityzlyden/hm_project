from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class Gender(DjangoChoices):
    male = ChoiceItem("male")
    female = ChoiceItem("female")
    not_specified = ChoiceItem("not specified")


class Match(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=13, choices=Gender.choices)

    def __str__(self):
        return self.first_name
