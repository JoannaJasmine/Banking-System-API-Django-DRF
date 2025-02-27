from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']  # Change from username to email
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)  # Authenticate with email

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # This will protect the endpoint
def protected_view(request):
    return Response({"message": "This is a protected view!"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    """
    View that returns the current logged-in user's data.
    """
    user = request.user
    return Response({
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_active': user.is_active,
        'date_joined': user.date_joined,
    })
