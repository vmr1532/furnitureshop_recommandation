"""myreviews URL Configuration

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
from django.conf.urls import include, url
from django.views.generic import RedirectView
from myfurniturereviews.models import FurnitureShop
from myfurniturereviews.models import Furnitures
from myfurniturereviews.models import FurnitureReview
from myfurniturereviews import views
from django.urls import re_path, include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from myfurniturereviews.models import FurnitureShop, Furnitures
from myfurniturereviews.forms import FurnitureShopForm, FurnituresForm
from myfurniturereviews.views import FurnitureShopCreate, FurnituresCreate, FurnitureShopDetail, review
from myfurniturereviews.models import FurnitureShop as furniturehop

urlpatterns = []
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.conf.urls import url, include
from django.contrib import admin
app_name = 'myfurnituresshop'

urlpatterns+=[
# List latest 5 restaurants: /myrestaurants/
    url(r'\^\$', 
        ListView.as_view(
        	queryset=FurnitureShop.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
        	context_object_name='latest_restaurant_list',
        	template_name='myfurniturereviews/furniture_shop.html'),
        name='furnitureshop_list'),

# Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'\^furnitureshop/(?P<pk>\d+)/\$',
        FurnitureShopDetail.as_view(),
        name='furnitureshop_detail'),

# Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'\^furnitureshop/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/\$',
        DetailView.as_view(
        	model=Furnitures,
        	template_name='myfurniturereviews/furniture_detail.html'),
        name='dish_detail'),

# Create a restaurant, /myrestaurants/restaurants/create/
    url(r'\^furnitureshop/create/\$',
        FurnitureShopCreate.as_view(),
        name='restaurant_create'),

# Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'\^furnitureshop/(?P<pk>\d+)/edit/\$',
        UpdateView.as_view(
        	model = FurnitureShop,
        	template_name = 'myfurniturereviews/form.html',
        	form_class = FurnitureShopForm),
        name='restaurant_edit'),

# Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'\^furnitureshop/(?P<pk>\\d+)/furnitures/create/\$',
    	FurnituresCreate.as_view(),
        name='dish_create'),

# Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'\^furnitureshop/(?P<pkr>\\d+)/dishes/(?P<pk>\\d+)/edit/\$',
    	UpdateView.as_view(
    		model = Furnitures,
    		template_name = 'myfurniturereviews/form.html',
    		form_class = FurnituresForm),
    	name='dish_edit'),

# Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    url(r'\^furnitureshop/(?P<pk>\\d+)/reviews/create/\$',
    	review,
    	name='review_create'),
]

urlpatterns = [
    url(r'^$', views.FurnitureShopDetail.as_view(template_name="myfurniturereviews/furnitureshop_list.html"),name= "myfurnitureshop"),
    path('login/', admin.site.urls),
    url(r'myfurnitureshops/',include('myfurniturereviews.urls')),
    ]
