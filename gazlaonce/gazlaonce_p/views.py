from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import categories,base_videos,base_category
from django.utils import timezone

def index(request):
    return render(request, "gazlaonce_p/index.html")

def videos(request):
    return render(request,"gazlaonce_p/videos.html")


def video_change(request):
    return render(request, "gazlaonce_p/video_change.html")


def get_data(request):
    category_id = request.GET.get('category_id')
    basecategory_id = request.GET.get('basecategory_id')
    videos_data = base_videos.objects.filter(categories=category_id,base_categories=basecategory_id).values('title', 'link', 'categories') 
    data = []
    for video in videos_data:
        data.append({
            'title': str(video['title']),
            'link': str(video['link']),
            'categories': str(video['categories'])
        })

    return JsonResponse(data, safe=False)

def get_data_subcategories(request ):
    basecategory_id = request.GET.get('basecategory_id')
    videos_data = categories.objects.filter(base_categories=basecategory_id,is_active="True").values('id', 'categoriesName','is_active') 
    data = []
    for video in videos_data:
        data.append({
            'id': str(video['id']),
            'categoriesName': str(video['categoriesName']),
            'is_active': str(video['is_active'])
        }) 
    return JsonResponse(data, safe=False)

def get_data_videos(request):
    category_id = request.GET.get('category_id')
    basecategory_id = request.GET.get('basecategory_id')
    videos_data = base_videos.objects.filter(categories=category_id,base_categories=basecategory_id).values('title', 'link', 'categories') 
    data = []
    for video in videos_data:
        data.append({
            'title': str(video['title']),
            'link': str(video['link']),
            'categories': str(video['categories'])
        })
    return JsonResponse(data, safe=False)

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        new_post = base_category(base_category_names=title,date_upload=timezone.now())
        new_post.save()

        return JsonResponse({'message': 'Ana kategori başarıyla kaydedildi.'})
    return JsonResponse({'message': 'Sadece POST istekleri kabul edilir.'})

def update_video_category(request):
    if request.method == "POST":
        video_id = request.POST.get("video_id")
        video_title = request.POST.get("videoName")
        video_link = request.POST.get("videoLink")
        base_categories_id = request.POST.get("base_categories_id")
        sub_categories_id = request.POST.get("sub_categories_id")
        try:
            item =  base_videos.objects.get(id=video_id)
            item.title = video_title
            item.link = video_link

            sub_category = categories.objects.get(id=int(sub_categories_id))
            base_category_asd = base_category.objects.get(id=int(base_categories_id))

            item.base_categories=base_category_asd
            item.categories=sub_category
            item.date_update = timezone.now()
            item.save()
            print(item)
            return JsonResponse({"message": "Kategori güncellendi."})
        except  base_videos.DoesNotExist:
            return JsonResponse({"message": "Kategori bulunamadı."})
    else:
        return JsonResponse({"message": "Geçersiz istek."})

def get_data_index_videos(request):   
    videos = base_videos.objects.all().order_by('-date_upload')[:10]
    video_data = []
    for video in videos:
        video_data.append({
            'link': video.link
        })
    return JsonResponse(video_data, safe=False)

