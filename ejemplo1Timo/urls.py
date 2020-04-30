"""ejemplo1Timo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from apps.usuarios.views import index,homeUser,category,singleVideo,singleStandard,styleGuide,contact,singleAudio,singleGallery,about

urlpatterns = [
    path('usuarios/', include('apps.usuarios.urls')),
    path('usuarios/', homeUser, name='homeuser'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about.html', about, name='about'),
    path('contact.html', contact, name='contact'),
    path('category.html', category, name='category'),
    path('single-audio.html', singleAudio, name='singleA'),
    path('single-gallery.html', singleGallery, name='singleG'),
    path('single-standard.html', singleStandard, name='singleS'),
    path('single-video.html', singleVideo, name='singleV'),
    path('style-guide.html', styleGuide, name='styleG'),
]
