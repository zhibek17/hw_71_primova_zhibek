from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('man', "Мужчина"),
        ('woman', "Женщина")
    ]
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар')
    user_information = models.TextField(null=True, blank=True, verbose_name='Информация о пользователе')
    phone_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='номер телефона')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='пол')
    publication_counter = models.PositiveIntegerField(default=0, verbose_name='счетчик публикаций')
    subscription_counter = models.PositiveIntegerField(default=0, verbose_name='счетчик подписок')
    subscriber_counter = models.PositiveIntegerField(default=0, verbose_name='счетчик подписчиков')
    subscriptions_users = models.ManyToManyField('accounts.User', related_name='subscribers_users',
                                                 verbose_name='подписки')