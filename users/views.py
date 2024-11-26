from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser, Role
from .serializers import UserSerializer, RoleSerializer

class RegisterView(APIView):
    permission_classes = []

    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected endpoint."})
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['role'] = user.role.name if user.role else "User"
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import Role, CustomUser

# Custom permission class to check if the user has specific permissions
class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required_permission = 'create_role'  # Adjust this according to your needs

        # Check if user has the required permission
        if not request.user.has_permission(required_permission):
            raise PermissionDenied("You do not have permission to perform this action.")
        return True

# Role management view (only accessible by users with 'create_role' permission)
# class RoleView(APIView):
#     permission_classes = [HasPermission]

#     def get(self, request):
#         roles = Role.objects.all()
#         return Response([role.name for role in roles])

#     def post(self, request):
#         name = request.data.get('name')
#         permissions = request.data.get('permissions')  # Comma-separated permissions
#         role = Role.objects.create(name=name, permissions=permissions)
#         return Response({"role": role.name}, status=201)

