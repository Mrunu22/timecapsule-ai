from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("Welcome to the Time Capsule API!")

urlpatterns = [
    path('', home),  # Root URL returns simple message
    path('admin/', admin.site.urls),
    path('api/', include('capsules.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#access: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4MDIwMDgyLCJpYXQiOjE3NDgwMTgyODIsImp0aSI6IjExNTIzZjIzODhhZjRhNzNiYjA2Y2NhYWEyMDU1MjUyIiwidXNlcl9pZCI6M30.5LtWelZ6R5Pu8TmbCLjoJruLcg_MqC4-Nwd5Cfl1cG4"

#"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0ODEwNDY4MiwiaWF0IjoxNzQ4MDE4MjgyLCJqdGkiOiI2ODhkMDVjYjRhMmU0ZTFmOWEwNTkwOGJlNmZkZTlkNyIsInVzZXJfaWQiOjN9.38gfJpVfAy5Tvyz36RaiF2NeHfabhcCFzijFFeHneL4",