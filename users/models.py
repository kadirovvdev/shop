from django.db import models
from django.contrib.auth.models import AbstractUser

ORDINARY_USER, ADMIN, MANAGER = ('ordinary_user', 'admin', 'manager')

NEW, CONFIRM, DONE, DONE_PHOTO = ('new', 'confirm', 'done', 'done_photo')

MALE, FEMALE, OTHER = ('male', 'female', 'other')

VIA_EMAIL, VIA_PHONE = ('via_email', 'via_phone')


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (ORDINARY_USER, ORDINARY_USER),
        (ADMIN, ADMIN),
        (MANAGER, MANAGER)
    )
    user_role = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default=ORDINARY_USER)
    USER_STATUS_CHOICES = (
        (NEW, NEW),
        (CONFIRM, CONFIRM),
        (DONE, DONE),
        (DONE_PHOTO, DONE_PHOTO)
    )
    user_status = models.CharField(max_length=50, choices=USER_STATUS_CHOICES, default=NEW)
    GENDER_CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER)
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username


class UserConfirm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    CONFIRMATION_METHOD_CHOICES = (
        (VIA_EMAIL, VIA_EMAIL),
        (VIA_PHONE, VIA_PHONE)
    )
    confirmation_method = models.CharField(max_length=50, choices=CONFIRMATION_METHOD_CHOICES, default=VIA_EMAIL)

    def __str__(self):
        return f"{self.user.username} - {self.confirmation_code}"


class Shared(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.username
