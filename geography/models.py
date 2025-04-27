from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        permissions = [('manage_geography', 'Can manage geographic data')]

class Continent(models.Model):
    name = models.CharField("Continent", max_length=100, unique=True)
    code = models.CharField("ISO Code", max_length=2, unique=True)  # e.g. 'AF' for Africa
    world_body = models.CharField("World Body", max_length=100, blank=True, null=True)  # New field
    sport_code = models.CharField ("Sport Code", max_length=50, blank=True, null=True)
    cont_federation = models.CharField ("Federation", max_length=100, blank=True, null=True)
    fedabrev = models.CharField("Fed Abrev", max_length=10, unique=True, null=True)  # e.g. 'AF' for Africa
    logo = models.ImageField(upload_to='continents/logos/', blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Toggle to show/hide this continent in lists.")

    def __str__(self):
        return f"{self.name} ({self.code})"

class Country(models.Model):
    name = models.CharField(max_length=100)

    code = models.CharField(max_length=3)  # ISO 3-letter code

    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
        limit_choices_to={'is_active': True}  # Only active continents
    )
    flag = models.ImageField(upload_to='countries/flags/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.continent.name})"

    def continent_logo(self):
        return self.continent.logo if self.continent.logo else None

        class Meta:
                verbose_name_plural = "countries"
                unique_together = [['name', 'continent'], ['code']]




