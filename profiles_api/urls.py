from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api.views import UserProfileViewset, UserLoginApiView, ProfileFeedItemViewset


router = DefaultRouter()
router.register('profiles', UserProfileViewset)
router.register('feed', ProfileFeedItemViewset)

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
