from rest_framework.permissions import BasePermission
from .models import StockTransaction


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, transaction):
        return request.user == transaction.shareholder
