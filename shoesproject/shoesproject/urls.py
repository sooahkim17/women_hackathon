"""shoesproject URL Configuration

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
from django.urls import path
import shoes.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',shoes.views.home,name='home'),
    path('suggestion/<int:suggestion_id>',shoes.views.suggestion_detail, name='suggestion_detail'),
    path('new/',shoes.views.suggestion_new,name='suggestion_new'),
    path('create/',shoes.views.create,name='create'),
    path('suggestion/',shoes.views.suggestion,name='suggestion'),
    path('suggestion/<int:suggestion_id>/delete/',shoes.views.delete,name='delete'),
    path('suggestion/<int:suggestion_id>/edit/',shoes.views.edit,name='edit'),
    path('suggestion/<int:suggestion_id>/update/',shoes.views.update,name='update'),
    path('home_detail/',shoes.views.post_list,name='search')
]





