from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import categories,base_videos,base_category
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test

def is_superuser(user):
    return user.is_authenticated and user.is_superuser == 1

@user_passes_test(is_superuser)
def subcategory_change(request):
    return render(request, "gazlaonce_p/subcategory_change.html")


def get_subcategories(request):
    categories1 =categories.objects.all()
    data = [{'categoriesName': category.categoriesName,'base_categories_name':category.base_categories.base_category_names,'is_active':category.is_active,'id': str(category.id)}
            for category in categories1]
    return JsonResponse(data, safe=False)


def create_post_subcategory(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        base_categoriesId = int(request.POST.get('base_categories_id'))

        print("title",title,"base id",base_categoriesId)
        base_category_instance = get_object_or_404(base_category, id=base_categoriesId)
        new_post = categories(categoriesName=title,base_categories=base_category_instance,date_upload=timezone.now())
        new_post.save()

        return JsonResponse({'message': 'Ana kategori başarıyla kaydedildi.'})
    return JsonResponse({'message': 'Sadece POST istekleri kabul edilir.'})


def delete_subcategory(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        categories.objects.filter(id=category_id).delete()
        return JsonResponse({"message": "Category deleted successfully."})
    
 
def update_sub_category_activity(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        is_active = request.POST.get("active")
        try:
            category =  categories.objects.get(id=category_id)
            category.is_active = is_active
            category.date_update = timezone.now()
            category.save()
            return JsonResponse({"message": "Kategori güncellendi."})
        except  categories.DoesNotExist:
            return JsonResponse({"message": "Kategori bulunamadı."})
    else:
        return JsonResponse({"message": "Geçersiz istek."})
    

def get_data_subcategories_list(request):
    base_category_list = base_category.objects.filter(is_active="True").values('id', 'base_category_names','is_active') 
    data = []
    for video in base_category_list:
        data.append({
            'id': str(video['id']),
            'base_category_names': str(video['base_category_names']),
            'is_active': str(video['is_active'])
        }) 
    return JsonResponse(data, safe=False)