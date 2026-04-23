from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel.name)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc.name)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc.name)

        # Activities
        Activity.objects.create(user=ironman.email, activity_type='run', duration=30, date='2026-04-20')
        Activity.objects.create(user=captain.email, activity_type='cycle', duration=45, date='2026-04-21')
        Activity.objects.create(user=batman.email, activity_type='swim', duration=25, date='2026-04-22')
        Activity.objects.create(user=superman.email, activity_type='fly', duration=60, date='2026-04-23')

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=150)
        Leaderboard.objects.create(team=dc.name, points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do 10 pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='easy')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
