from rest_framework.permissions import BasePermission
from users.models import User


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, user):
        return request.user == user
