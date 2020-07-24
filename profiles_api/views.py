from rest_framework import viewsets, filters
from rest_framework.response import Response
from .serializers import ProfileSerializer, ProfileFeedSerializer
from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, ProfileFeedPermissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserProfileViewset(viewsets.ModelViewSet):
    """ViewSet to handle api endpoint for UserProfile model"""
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemViewset(viewsets.ModelViewSet):
    """Viewset to control the profile feed item endpoint"""
    serializer_class = ProfileFeedSerializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ProfileFeedPermissions, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('status_text',)

    def perform_create(self, serializer):
        """overrides the serializer.save() in the built in create()"""
        serializer.save(user_profile=self.request.user)
