from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='1234', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='1234', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='1234', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='1234', team=dc)
        bruce_dc = User.objects.create_user(username='batman', email='bruce@dc.com', password='1234', team=dc)

        # Crear actividades
        Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='bike', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        Activity.objects.create(user=clark, type='run', duration=50, calories=450)
        Activity.objects.create(user=bruce_dc, type='bike', duration=40, calories=350)

        # Crear leaderboard
        Leaderboard.objects.create(user=tony, points=1000)
        Leaderboard.objects.create(user=steve, points=900)
        Leaderboard.objects.create(user=bruce, points=800)
        Leaderboard.objects.create(user=clark, points=950)
        Leaderboard.objects.create(user=bruce_dc, points=850)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', duration=60)
        Workout.objects.create(name='Cardio', description='Entrenamiento cardiovascular', duration=45)
        Workout.objects.create(name='Strength', description='Entrenamiento de fuerza', duration=50)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
