"""backend URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken.models import Token
from library.views import *
from todo.views import *

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookViewSet)
router.register('bios', BioViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoViewSet)
router.register('users', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', obtain_auth_token),
    path('api_get/', get_view),
    path('api_post/', post_view),
    path('api_get2/', get_view2),
    path('api_post2/', post_view2)
]



