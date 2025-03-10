from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(
        max_length=50, verbose_name="имя", help_text="Укажите имя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=50, verbose_name="фамилия", help_text="Укажите фамилию", **NULLABLE
    )
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Укажите почту"
    )

    is_active = models.BooleanField(default=False)



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email
