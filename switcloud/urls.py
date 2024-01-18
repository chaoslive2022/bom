"""
URL configuration for switcloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from integrators.api.v1.views import (
    IntegratorViewSet, 
    ContractViewSet
)
from pops.api.v1.views import (
    MerchantViewSet,
    LocationViewSet,
    PointOfPaymentViewSet
)
from configurations.api.v1.views import EMVConfigurationViewSet
from profiles.api.v1.views import (
    UserProfileViewSet,
    UserLoginApiView
)

# maps urls to DRF's controllers
router = routers.DefaultRouter()
router.register(r'integrators', IntegratorViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'configurations', EMVConfigurationViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'merchants', MerchantViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'pops', PointOfPaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', UserLoginApiView.as_view()),
    path('api/', include(router.urls)),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
