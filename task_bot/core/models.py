from django.db import models

# Create your models here.
#TelegramUser Model
from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - @{self.telegram_username}"
