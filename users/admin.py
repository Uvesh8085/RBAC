from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser,Role

# Register your models here.
admin.site.register(CustomUser)

# Create roles and assign permissions
# admin_role = Role.objects.create(name='Admin', permissions='create_role, delete_role, manage_roles')
# moderator_role = Role.objects.create(name='Moderator', permissions='view_role, manage_roles')
# user_role = Role.objects.create(name='User', permissions='view_role')

# # Assign roles to users
# user = CustomUser.objects.create_user(username='testuser', password='password123')
# user.role = admin_role  # Assign Admin role
# user.save()
