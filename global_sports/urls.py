from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


# Test view for root URL
def health_check(request):
    return HttpResponse("System OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', admin.site.login, name='admin-login'),
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
     path('admin/logout/', RedirectView.as_view(url='/admin/login/', permanent=False), name='admin-logout'),
    path('geography/', include('geography.urls')),
    path('', lambda r: HttpResponse("System OK")),
    path('', health_check),  # Root URL test
    # Keep geography/ commented for now
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/admin/login/'), name='logout'),


]