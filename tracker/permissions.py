from rest_framework.permissions import BasePermission



# Custom permission to allow only the record owner or an admin
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view,  obj):
        return request.user and (obj.user == request.user or request.user.is_staff)
