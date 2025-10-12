from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import os

load_dotenv(override=True)


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email=os.getenv('ADMINEMAIL'),
            first_name='Admin',
            last_name='Adminex'
        )
        user.set_password(os.getenv('ADMINPASSWORD'))
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user with email {user.email}'))
