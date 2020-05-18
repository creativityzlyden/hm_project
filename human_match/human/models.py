from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class Gender(DjangoChoices):
    not_specified = ChoiceItem("not specified")
    male = ChoiceItem("male")
    female = ChoiceItem("female")


class Human(models.Model):
    avatar = models.ImageField(upload_to='avatar/', height_field=None, width_field=None, max_length=100, null=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=13, choices=Gender.choices)

    def __str__(self):
        return self.first_name
