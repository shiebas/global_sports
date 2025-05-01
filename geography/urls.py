from django.urls import path
from . import views

urlpatterns = [
     path('test-auth/', views.test_auth, name='test-auth')
#    path('get-bodies/', views.get_regional_bodies, name='get-regional-bodies'),
]
