from django.urls import path
from .views import (
    RegisterView, RoleView, LogoutView, ProtectedView, CustomTokenObtainPairView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('roles/', RoleView.as_view(), name='roles'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
