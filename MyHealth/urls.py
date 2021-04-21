"""MyHealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from HealthRecord.views import get_current_time,login, home, HealthHome, create_account, thanks, user_profile
from django.conf.urls.static import static
import API.urls


urlpatterns = [
    
    path('',home),
    path('api/',include(API.urls)),
    path('HealthRecord/',include('HealthRecord.urls')),
    path('current_time/',get_current_time,name='current_time'),
    path('login/',login,name='login'),
    path('create_account/',create_account,name='create_account'),
    path('login/create_account/',create_account,name='create_account'),
    path('login/create_account/thanks/',thanks,name='thanks_to_register'),
    path('login/create_account/thanks/HealthRecord/',home),
    path('login/user_profile/',user_profile,name='profile'),
    path('admin/', admin.site.urls),
    path('home_page/',HealthHome.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)