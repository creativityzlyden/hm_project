import os
import django
import random
import sys


path = '/hm_project/human_match'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'human_match.settings')

django.setup()

from faker import Faker
from human.models import Human


def create_match(n):
    fake = Faker(['en_US'])
    for _ in range(n):
        id = random.randint(1, 100)
        avatar = fake.image_url()
        first_name = fake.first_name()
        second_name = fake.last_name()
        gender = random.choice(['male', 'female', 'not specified'])
        age = random.randint(18, 60)
        Human.objects.create(id=id, first_name=first_name,
                             avatar=avatar,
                             second_name=second_name,
                             age=age, gender=gender)


create_match(5)
print("OK")
