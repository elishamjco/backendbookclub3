from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer  # Replace with the actual path to your user serializer
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[v1])}
        except (TypeError, KeyError):
            return {}

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
