from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib import admin
from myfurniturereviews.models import FurnitureShop
from myfurniturereviews.models import Furnitures
from myfurniturereviews.models import FurnitureReview
from myfurniturereviews.forms import FurnitureShopForm, FurnituresForm

class FurnitureDetail(DetailView):
  model = FurnitureShop
  template_name = 'myrestaurants/furnitureshop_detail.html'

  def get_context_data(self, **kwargs):
    context = super(RestaurantDetail, self).get_context_data(**kwargs)
    context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
    return context

class FurnitureShopCreate(CreateView):
  model = FurnitureShop
  template_name = 'myrfurnitureshop/form.html'
  form_class = FurnitureShopForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(FurnitureShopCreate, self).form_valid(form)

class FurnituresCreate(CreateView):
  model = Furnitures
  template_name = 'myrfurnitureshop/form.html'
  form_class = FurnituresForm
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.furnitureshop = FurnitureShop.objects.get(id=self.kwargs['pk'])
    return super(DishCreate, self).form_valid(form)

def review(request, pk):
  FurnitureShop = get_object_or_404(FurnitureShop, pk=pk)
  review = RestaurantReview(
      rating=request.POST['rating'],
      comment=request.POST['comment'],
      user=request.user,
      furnirureshop =furnirureshop)
  review.save()
  return HttpResponseRedirect(reverse('myrfurnitureshop:furnitureshop_detail', args=(furnitureshop.id,)))
