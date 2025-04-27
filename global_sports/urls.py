from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

# Test view for root URL
def health_check(request):
    return HttpResponse("System OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geography/', include('geography.urls')),
    path('', lambda r: HttpResponse("System OK")),
    path('', health_check),  # Root URL test
    # Keep geography/ commented for now
]