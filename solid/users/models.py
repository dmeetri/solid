from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserModel(AbstractUser):
    email = None
    first_name = None
    last_name = None

    class Status(models.TextChoices):
        FREE = 'FREE', 'Свободен'
        BUSY = 'BUSY', 'Занят'
        VACATION = 'VACATION', 'В отпуске'

    status = models.CharField(
        choices=Status.choices,
        default=Status.FREE,
    )
