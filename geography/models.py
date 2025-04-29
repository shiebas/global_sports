from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

class User(AbstractUser):
    class Meta:
        permissions = [('manage_geography', 'Can manage geographic data')]

class Continent(models.Model):
    name = models.CharField("Continent", max_length=100, unique=True)
    code = models.CharField("ISO Code", max_length=2, unique=True)  # e.g. 'AF' for Africa
    world_body = models.CharField("World Body", max_length=100, blank=True, null=True)  # New field
    sport_code = models.CharField ("Sport Code", max_length=50, blank=True, null=True)
    cont_federation = models.CharField (verbose_name ="Continental Body" , max_length=100, blank=True, null=True)
    fedabrev = models.CharField("Fed Abrev", max_length=10, unique=True, null=True)  # e.g. 'AF' for Africa
    logo = models.ImageField(upload_to='continents/logos/', blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Toggle to show/hide this continent in lists.")

    def __str__(self):
        return f"{self.name} ({self.code})"

class RegionalBody(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='regional_bodies')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)  # ISO 3-letter code
    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
        limit_choices_to={'is_active': True}
    )
    regional_body = models.ForeignKey(RegionalBody, on_delete=models.SET_NULL, null=True, blank=True)
    flag = models.ImageField(upload_to='countries/flags/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "countries"
        unique_together = [['name', 'continent'], ['code']]

    def __str__(self):
        return self.name

def display_flag(self, obj):
    image_url = obj.flag.url if obj.flag else static('admin/img/logo.png')
    return format_html('<img src="{}" width="60" style="border-radius:2px">', image_url)
display_flag.short_description = 'Flag'

@property
def country_body(self):
    """Returns the appropriate football body - regional if set, otherwise continental"""
    if self.regional_body is not None:
        return self.regional_body.code
    else:
        return self.continent.cont_federation






