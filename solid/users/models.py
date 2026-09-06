from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    email = None
    first_name = None
    last_name = None
