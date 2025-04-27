from django.urls import path
from . import views

app_name = 'geography'

urlpatterns = [
    # Basic test route
    path('test/', views.test_view, name='test-view'),
]