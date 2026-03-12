import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

SUPERUSERS = [
    {"first_name": "Troey", "last_name": "Sambu", "email": "sambutroey231@gmail.com",
     "password_env": "TROEY_PASSWORD", "default_password": "TroeyAdmin2026!"},
    {"first_name": "Silvia", "last_name": "Wairimu", "email": "silvia@trovia.co.ke",
     "password_env": "SILVIA_PASSWORD", "default_password": "SilviaAdmin2026!"},
]

class Command(BaseCommand):
    help = "Create Trovia founder superuser accounts (Troey & Silvia)"

    def handle(self, *args, **options):
        for su in SUPERUSERS:
            if User.objects.filter(email=su["email"]).exists():
                self.stdout.write(self.style.WARNING(f"User '{su['email']}' already exists – skipping."))
                continue
            password = os.environ.get(su["password_env"], su["default_password"])
            user = User.objects.create_superuser(
                username=su["first_name"].lower(),
                email=su["email"],
                password=password,
                first_name=su["first_name"],
                last_name=su["last_name"],
            )
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser created: {user.first_name} <{user.email}>"))
