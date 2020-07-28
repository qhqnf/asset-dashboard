from rest_framework.permissions import BasePermission
from users.models import User


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(pk=view.kwargs["pk"])
        return request.user == user
