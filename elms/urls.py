"""
URL configuration for elms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from mainapp.views import *
from adminapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from studentapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name='index'),
    path('contact/',contactus,name='contactus'),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('adminhome/',adminhome,name='adminhome'),
    path('adminlogout/',adminlogout,name='adminlogout'),
    path('viewenquiries/',viewenquiries,name='viewenquiries'),
    path('deleteenq/<id>',deleteenq,name='deleteenq'),
    path('studentdata/',studentdata,name='studentdata'),
    path('viewmore/<rollno>',viewmore,name='viewmore'),
    path('changepassword/',changepassword,name='changepassword'),
    path('addmaterial/',addmaterial,name='addmaterial'),
    path('viewmaterial/',viewmaterial,name='viewmaterial'),
    path('deletemat/<mid>',deletemat,name='deletemat'),
    path('studenthome/',studenthome,name="studenthome"),
    path('studentlogout/',studentlogout,name="studentlogout"),
    path('changepwd/',changepwd,name="changepwd"),
    path('viewmat/',viewmat,name="viewmat"),
    path('giveresponse/',giveresponse,name="giveresponse"),
    path('viewfeedback/',viewfeedback,name='viewfeedback'),
    path('viewcomplaint/',viewcomplaint,name='viewcomplaint'),
    path('deletefeedback/<id>',deletefeedback,name='deletefeedback'),
    path('deletecomp/<id>',deletecomp,name='deletecomp'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)