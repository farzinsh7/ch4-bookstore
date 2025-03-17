from django.db import models
from ..validators import iranian_phone_number_validator


class Profile(models.Model):
    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="user_profile"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=15, validators=[iranian_phone_number_validator]
    )
    avatar = models.ImageField(
        upload_to="accounts/profile/", default="profile/default.jpg"
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    def get_fullname(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "پروفایل خود را تکمیل کنید"
