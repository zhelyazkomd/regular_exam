from django.core.validators import MinValueValidator
from django.db import models

from regular_exam.web.validator import min_length_validator, min_and_max_year_validation


class Profile(models.Model):
    MAX_PASSWORD_LENGTH = 30
    MAX_USERNAME_LENGTH = 10
    MIN_AGE_VALUE = 18

    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        blank=False,
        null=False,
        validators=(
            min_length_validator,
        )
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(MIN_AGE_VALUE),
        )
    )
    passwords = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name='First Name',

    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name='Last Name',

    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )

    @property
    def name_generator(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return f'{self.first_name}'
        elif self.last_name:
            return f'{self.last_name}'


class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MAX_MODEL_LENGTH = 20
    MIN_MODEL_LENGTH = 2

    MIN_PRICE_VALUE = 1

    CARS_TYPE = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )
    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        blank=False,
        null=False,
        choices=CARS_TYPE,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        blank=False,
        null=False,
        validators=(
            min_length_validator,
        )
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            min_and_max_year_validation,
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(MIN_PRICE_VALUE),
        )
    )

    class Meta:
        ordering = ('pk',)