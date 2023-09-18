from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import base_category
from django.utils import timezone

def base_category_change(request):
    return render(request, "gazlaonce_p/base_category_change.html")


def get_data_base_category(request):
    videos_data = base_category.objects.filter(is_active="True").values('base_category_names','id') 
    data = []
    for video in videos_data:
        data.append({
            'base_category_names': str(video['base_category_names']),
            'id': str(video['id']),
        })
    return JsonResponse(data, safe=False)


def get_categories(request):
    categories = base_category.objects.all()
    data = [{'categoriesName': category.base_category_names, 'is_active': category.is_active, 'id': str(category.id)} for category in categories]
    return JsonResponse(data, safe=False)

