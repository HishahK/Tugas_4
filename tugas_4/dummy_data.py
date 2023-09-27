import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tugas_4.settings")

import django
django.setup()

from django.contrib.auth.models import User
from tugas_4 import Item

def create_dummy_data():
    # Membuat 2 akun pengguna
    user1 = User.objects.create_user(username='user1', password='password123')
    user2 = User.objects.create_user(username='user2', password='password123')
    
    # Membuat 3 dummy data untuk setiap akun
    Item.objects.create(user=user1, name='Item1_User1', description='Description1')
    Item.objects.create(user=user1, name='Item2_User1', description='Description2')
    Item.objects.create(user=user1, name='Item3_User1', description='Description3')
    
    Item.objects.create(user=user2, name='Item1_User2', description='Description1')
    Item.objects.create(user=user2, name='Item2_User2', description='Description2')
    Item.objects.create(user=user2, name='Item3_User2', description='Description3')

if __name__ == '__main__':
    create_dummy_data()
