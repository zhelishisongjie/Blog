"""
URL configuration for djangoBlog project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import     path, include


import comment.views
import userprofile.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("article/" ,   include("article.urls")),


    path("login/" ,     userprofile.views.user_login , name = "login"),
    path("logout/",     userprofile.views.user_logout , name = "logout"),
    path("register/",   userprofile.views.user_register , name = "register"),
    path("comment/<int:article_id>/" , comment.views.post_comment , name = "post_comment"),

    path('mdeditor/',    include('mdeditor.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)