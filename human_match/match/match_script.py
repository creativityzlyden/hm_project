import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'human_match.settings')
django.setup()

from faker import Faker
from .models import Match


def create_match(N):
    fake = Faker()
    for _ in range(N):
        id = random.randint(1, 10)
        first_name = models.CharField(max_length=100)
        second_name = models.CharField(max_length=100)
        age = models.CharField(max_length=3)
        gender = models.CharField(max_length=13, choices=Gender.choices)

