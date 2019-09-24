from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantDetail, review

urlpatterns = [

# List latest 5 restaurants: /myrestaurants/
    url(r'\^\$', 
        ListView.as_view(
        	queryset=FurnitureShop.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
        	context_object_name='latest_restaurant_list',
        	template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),

# Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'\^furnitureshop/(?P<pk>\d+)/\$',
        FurnitureDetail.as_view(),
        name='restaurant_detail'),

# Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'\^furnitureshop/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/\$',
        DetailView.as_view(
        	model=Dish,
        	template_name='myrestaurants/furniture_detail.html'),
        name='dish_detail'),

# Create a restaurant, /myrestaurants/restaurants/create/
    url(r'\^furnitureshop/create/\$',
        furnitureshopCreate.as_view(),
        name='restaurant_create'),

# Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'\^furnitureshop/(?P<pk>\d+)/edit/\$',
        UpdateView.as_view(
        	model = FurnitureShop,
        	template_name = 'myfurniture/form.html',
        	form_class = FurnitureShopForm),
        name='restaurant_edit'),

# Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'\^furnitureshop/(?P<pk>\\d+)/furnitures/create/\$',
    	FurnitureCreate.as_view(),
        name='dish_create'),

# Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'\^furnitureshop/(?P<pkr>\\d+)/dishes/(?P<pk>\\d+)/edit/\$',
    	UpdateView.as_view(
    		model = furnitures,
    		template_name = 'myfurniture/form.html',
    		form_class = furnitureForm),
    	name='dish_edit'),

# Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    url(r'\^furnitureshop/(?P<pk>\\d+)/reviews/create/\$',
    	review,
    	name='review_create'),
]