def country_names(request):
    """Makes country model names available in templates"""
    try:
        from geography.models import Country
        return {
            'country_verbose_name': Country._meta.verbose_name,
            'country_verbose_name_plural': Country._meta.verbose_name_plural
        }
    except:
        return {}  # Fails gracefully if model isn't available