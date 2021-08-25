from django.shortcuts import render
from .models import Meals,Category
# Create your views here.

def meal_list(request):
    context={
        "meal_lists":Meals.objects.all(),
        "name":"Meal List",
        "categories":Category.objects.all
    }
    return render(request,"meals/meal_list.html",context)
    
def meal_detail(request,slug):
    meal_detail=Meals.objects.get(slug=slug)
    context={
        "meal_detail":meal_detail,
        "name":"Meal Details"
        }
    return render(request,"meals/meal_detail.html",context)
