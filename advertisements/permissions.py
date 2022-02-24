from rest_framework.permissions import BasePermission, SAFE_METHODS

#Ограничение на удаление и изменение, у админов полные права
from .models import AdvertisementStatusChoices


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS or request.user.is_staff:
            return True
        return obj.creator == request.user
