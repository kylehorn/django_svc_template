from rest_framework import permissions
from django.contrib.auth.models import User
from user_profile.models import UserProfile


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        class_name = obj.__class__.__name__

        if class_name == User.__name__:
            return True

        if class_name == UserProfile.__name__:
            return obj.user == request.user

        return False
