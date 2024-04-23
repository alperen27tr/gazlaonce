from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import categories,base_videos,base_category
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def video_change(request):
    return render(request, "gazlaonce_p/video_change.html")

def videoUpdateGet(request):
    videoId = request.GET.get('videoId')
    print("----------"+videoId)
    videos = base_videos.objects.filter(id=videoId).values('title', 'link', 'categories','base_categories').first() 
    print("+++++++++"+videos['title'])
    data = []
    data.append({
        'title': videos['title'],
        'link': videos['link'],
        'categories': videos['categories'],
        'base_categories': videos['base_categories']
    })
    return JsonResponse(data, safe=False)

def create_post_video(request):
    if request.method == 'POST':
        title = request.POST.get('videoName')
        link = request.POST.get('videoLink')
        base_categories_id = request.POST.get("base_categories_id")
        sub_categories_id = request.POST.get("sub_categories_id")

        sub_category = categories.objects.get(id=int(sub_categories_id))
        base_category_asd = base_category.objects.get(id=int(base_categories_id))

        new_post = base_videos(title=title,link=link,base_categories=base_category_asd,categories=sub_category)
        new_post.save()
        return JsonResponse({'message': 'Video başarıyla kaydedildi.'})
    return JsonResponse({'message': 'Sadece POST istekleri kabul edilir.'})

def get_data_changevideos(request):
    data = base_videos.objects.all()  
    for changevideos in data:        
        print(changevideos.is_active)
    data_list =[{'id':changevideos.id, 'title': changevideos.title,'link':changevideos.link,'base_categories_id':changevideos.base_categories.id,'base_categories_names':changevideos.base_categories.base_category_names,'is_active':changevideos.is_active,'categories_id':changevideos.categories.id,'categories_name':changevideos.categories.categoriesName}
                 for changevideos in data]
    
    return JsonResponse(data_list, safe=False)

def delete_base_videos_admin(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        base_videos.objects.filter(id=category_id).delete()
        return JsonResponse({"message": "Category deleted successfully."})
    

def update_video_admin(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        category_name = request.POST.get("category_name")
        try:
            category =  base_videos.objects.get(id=category_id)
            category.link = category_name
            category.title = category_name
            category.date_update = timezone.now()
            category.save()
            return JsonResponse({"message": "Kategori güncellendi."})
        except  base_videos.DoesNotExist:
            return JsonResponse({"message": "Kategori bulunamadı."})
    else:
        return JsonResponse({"message": "Geçersiz istek."})
    

def video_gallery_index(request):
    data = base_videos.objects.filter(is_active = 1).order_by('?')[:16]
    data_list = []
    for item in data:
        data_list.append({
            'title': item.title,
            'link': item.link,
        })
    return JsonResponse(data_list, safe=False)


def update_videos_activity(request):
    if request.method == "POST":
        video_id = request.POST.get("video_id")
        is_active = request.POST.get("active")
        try:
            video = base_videos.objects.get(id=video_id)
            video.is_active = str(is_active)
            video.date_update = timezone.now()
            video.save()
            return JsonResponse({"message": "Kategori güncellendi."})
        except  base_videos.DoesNotExist:
            return JsonResponse({"message": "Kategori bulunamadı."})
    else:
        return JsonResponse({"message": "Geçersiz istek."})


def get_motocycle_videos(request):
    videos = base_videos.objects.filter(id=1, base_categories=1)
    video_list = list(videos)
    return JsonResponse({'videos': video_list})


def get_data_opened_video_page_videos(request):
    basecategory_id = request.GET.get('basecategory_id')
    videos_data = base_videos.objects.filter(base_categories=str(basecategory_id)).order_by('?')[:20]
    data = []
    for video in videos_data:
        data.append({
            'id': str(video.id),  
            'title': video.title,  
            'link': video.link,  
            'is_active': video.is_active, 
        })
    return JsonResponse(data, safe=False)













