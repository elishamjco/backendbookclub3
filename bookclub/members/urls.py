from django.urls import path
from .views import UserRegisterApiView

urlpatterns = [
    path('api/register/', UserRegisterApiView.as_view(), name='register-api'),
]