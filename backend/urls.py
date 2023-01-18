"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/unfollow/', include('unfollow.urls')),
    path('api/client/', include('client.urls')),
    path('api/feather/', include('feather.urls')),
    path('api/twitter/', include('twitter.urls')),
    path('api/admin/', include('appadmin.urls')),
    path('api/garden/', include('gardens.urls')),
    path('api/bookmarks/', include('bookmarks.urls')),
    path('api/followed/', include('followed.urls')),
    path('api/podcast/', include('podcast_toolkit.urls')),
    path('api/search/', include('search.urls')),
    path('webhooks/', include('webhooks.urls')),
]
