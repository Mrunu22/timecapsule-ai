from django.urls import path
from .views import RegisterView, CapsuleCreateView, CapsuleListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('capsules/', CapsuleListView.as_view(), name='capsule-list'),
    path('capsules/create/', CapsuleCreateView.as_view(), name='capsule-create'),
]
