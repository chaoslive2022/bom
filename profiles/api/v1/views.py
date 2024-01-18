from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles import models
from . import serializers
from profiles import permissions

#login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    #how user is authenticated, i.e. only 1 method here = TokenAuthentication
    authentication_classes = (TokenAuthentication,)
    #how user gets permission to perform accesses
    permission_classes = (permissions.UpdateOwnProfile,)
    # search profiles feature, i.e. only 1 filer here
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


#Class ObtainAuthToken could be added as is in urls.py
#But it doesn't enable itself by default into browserable admin site
#So, we need to overwrite this class here
class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES