"""
URL configuration for VanEshop project.

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
from django.conf import settings
from django.conf.urls.static import static

import Eshop.views
import members.views

urlpatterns = [
    path('/', Eshop.views.vans, name="vans"),
    path('vans/', Eshop.views.vans, name="vans"),
    path('contact/', Eshop.views.contact, name="contact"),
    path('vans/<int:id>',Eshop.views.vans_detail_view),
    path('vans/edit/<int:id>',Eshop.views.editvan, name='editvan'),
    path('vans/delete/<int:id>',Eshop.views.deletevan, name='deletevan'),
    path('vans/addvan/', Eshop.views.addvan, name="addvan"),
    path('vans/form/makereservation/<int:id>', Eshop.views.makereservation, name="makereservation"),
    path('vans/form/rentvan/<int:id>', Eshop.views.rent, name="rent"),
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('signin_user/', members.views.signin_user, name="signin"),
    path('login_user/', members.views.login_user, name="login"),
    path('logout_user/', members.views.logout_user, name="logout")
    

    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

