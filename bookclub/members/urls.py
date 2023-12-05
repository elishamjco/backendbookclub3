from django.urls import path
from .views import UserRegisterApiView, UserRegisterView

urlpatterns = [
    path('api/register/', UserRegisterApiView.as_view(), name='register-api'),
    path('register/', UserRegisterView.as_view(), name="register"),
]