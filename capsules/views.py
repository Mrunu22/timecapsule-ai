from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, CapsuleSerializer
from .models import Capsule
from django.utils.timezone import now

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Capsule Creation View
class CapsuleCreateView(generics.CreateAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Capsule Listing View (only unlocked ones)
class CapsuleListView(generics.ListAPIView):
    serializer_class = CapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Capsule.objects.filter(owner=self.request.user, unlock_date__lte=now()).order_by('-unlock_date')
