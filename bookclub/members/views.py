from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer  # Replace with the actual path to your user serializer

class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[API_VERSION])}
        except (TypeError, KeyError):
            return {}