from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import base_category
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test



def is_superuser(user):
    return user.is_authenticated and user.is_superuser == 1

@user_passes_test(is_superuser)
def base_category_change(request):
    return render(request, "gazlaonce_p/base_category_change.html")



def get_data_base_category1(request):
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


def get_data_header(request):
    basecategory_id = request.GET.get('basecategory_id')
    videos_data = base_category.objects.filter(id=basecategory_id,is_active="True").values('base_category_names') 
    data = []
    for video in videos_data:
        data.append({
            'base_category_names': str(video['base_category_names']),
        })       
    return JsonResponse(data, safe=False)


def base_category_list_view(request):
    return render(request, 'base_category_list.html')

def delete_category(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        base_category.objects.filter(id=category_id).delete()
        return JsonResponse({"message": "Category deleted successfully."})
    
def update_category(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        category_name = request.POST.get("category_name")
        print(category_name)
        try:
            category =  base_category.objects.get(id=category_id)
            category.base_category_names = category_name
            category.date_update = timezone.now()
            category.save()
            return JsonResponse({"message": "Kategori güncellendi."})
        except  base_category.DoesNotExist:
            return JsonResponse({"message": "Kategori bulunamadı."})
    else:
        return JsonResponse({"message": "Geçersiz istek."})
    

def update_base_category_activity(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        is_active = request.POST.get("active")
        try:
            category =  base_category.objects.get(id=category_id)
            category.is_active = is_active
            category.date_update = timezone.now()
            category.save()
            return JsonResponse({"message": "Kategori güncellendi."})
        except  base_category.DoesNotExist:
            return JsonResponse({"message": "Kategori bulunamadı."})
    else:
        return JsonResponse({"message": "Geçersiz istek."})
    

