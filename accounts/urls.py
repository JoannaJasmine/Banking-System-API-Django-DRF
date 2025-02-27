from django.urls import path
from .views import register, login, protected_view, current_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register),  # For registration endpoint
    path('login/', login),        # For login endpoint
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For obtaining JWT tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing JWT tokens
    path('protected/', protected_view),
    path('api/current_user/', current_user, name='current_user'),
]
