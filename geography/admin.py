from django.contrib import admin
from .models import Continent, Country

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'continent', 'code')
    list_select_related = ('continent',)

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)