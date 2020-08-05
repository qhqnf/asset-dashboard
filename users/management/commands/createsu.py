from django.core.management.base import BaseCommand
from users.models import User


class Commnad(BaseCommand):
    def handle(self, *args, **kwargs):
        admin = User.objects.get_or_none(username="ebadmin")
        if admin is None:
            User.objects.create_superuser("ebadmin", "didguscjf95@naver.com", "123")
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser Exists"))
