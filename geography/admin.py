from django.contrib import admin
from django.templatetags.static import static
from .models import Continent, Country, RegionalBody, User
from django.utils.html import format_html
from django import forms
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import logging
from django.contrib.auth.admin import UserAdmin

##from django.contrib.admin import ModelAdmin

# Get logger instance
logger = logging.getLogger(__name__)

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter regional bodies based on selected continent
        if 'continent' in self.data:
            try:
                continent_id = int(self.data.get('continent'))
                self.fields['regional_body'].queryset = RegionalBody.objects.filter(continent_id=continent_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['regional_body'].queryset = self.instance.continent.regional_bodies.all()

class RegionalBodyInline(admin.TabularInline):
    model = RegionalBody
    extra = 1

class RegionalBodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'continent')
    list_filter = ('continent',)

def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get-bodies/',
                csrf_exempt(self.admin_site.admin_view(self.get_bodies)),
                name='get_bodies'
            ),
        ]
        return custom_urls + urls

def get_bodies(self, request):
        """Production-safe endpoint"""
        continent_id = request.GET.get
        logger.info(f"Regional bodies requested for continent {continent_id}")

        if not continent_id or not continent_id.isdigit():
            logger.warning(f"Invalid continent ID: {continent_id}")
            return JsonResponse([], safe=False)

        bodies = RegionalBody.objects.filter(
            continent_id=int(continent_id)
            ).values('id', 'name')

        logger.debug(f"Returning {len(bodies)} bodies for continent {continent_id}")

        return JsonResponse(list(bodies), safe=False)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')




class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'world_body', 'cont_federation', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')
    inlines = [RegionalBodyInline]


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'continent', 'regional_body', 'display_flag')
    readonly_fields = ('display_flag',)
    list_filter = ('continent', 'regional_body')
    search_fields = ('name', 'code')

    class Media:
        js = ('js/country_admin.js',)

    def country_body_display(self, obj):
        return obj.country_body
    country_body_display.short_description = 'Football Body'

    def display_flag(self, obj):
        if obj.flag:
            return format_html(
                '<img src="{}" width="60">',
                obj.flag.url
            )
        return format_html(
            '<img src="{}" width="60">',
            static('admin/img/logo.png')  # SAFA fallback
        )
    display_flag.short_description = 'Flag'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opts.verbose_name_plural = "countries"



admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(User, CustomUserAdmin)