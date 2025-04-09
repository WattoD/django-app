"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# from django_api.views import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('members/', include('members.urls')),
    path('tags/', include('tags.urls')),
    path('languages/', include('languages.urls')),
    path('api/', include('django_api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token/obtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token-auth/', CustomAuthToken.as_view(), name='token-auth'),
    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
