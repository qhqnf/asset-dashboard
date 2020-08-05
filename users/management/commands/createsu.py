from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            admin = User.objects.get(username="ebadmin")
        except User.objects.DoesNotExist:
            admin = None
        if admin is None:
            User.objects.create_superuser("ebadmin", "didguscjf95@naver.com", "123")
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser Exists"))
