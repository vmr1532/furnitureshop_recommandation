from django.forms import ModelForm
from myfurniturereviews.models import FurnitureShop
from myfurniturereviews.models import Furnitures
from myfurniturereviews.models import FurnitureReview

class FurnitureShopForm(ModelForm):
  class Meta:
    model = FurnitureShop
    exclude = ('user', 'date',)

class FurnituresForm(ModelForm):
  class Meta:
    model = Furnitures
    exclude = ('user', 'date', 'restaurant',)
