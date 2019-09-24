from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myfurniturereviews.models import FurnitureShop
from myfurniturereviews.models import Furnitures
from myfurniturereviews.models import FurnitureReview




admin.site.register(FurnitureShop)
admin.site.register(Furnitures)
admin.site.register(FurnitureReview)
