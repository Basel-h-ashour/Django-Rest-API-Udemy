from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Restrict users to change their own profiles only"""

    def has_object_permission(self, request, view, obj):
        """Called by default each time a request is made to the api endpoint"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class ProfileFeedPermissions(permissions.BasePermission):
    """Controls the permissions of a profile feed object"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.user_profile.id