from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import categories,base_videos,base_category
from django.utils import timezone

def index(request):
    return render(request, "gazlaonce_p/index.html")

def videos(request):
    return render(request,"gazlaonce_p/videos.html")


def subcategory_change(request):
    return render(request, "gazlaonce_p/subcategory_change.html")

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


def get_data_header(request):
    basecategory_id = request.GET.get('basecategory_id')
    videos_data = base_category.objects.filter(id=basecategory_id,is_active="True").values('base_category_names') 
    data = []
    for video in videos_data:
        data.append({
            'base_category_names': str(video['base_category_names']),
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


def get_subcategories(request):
    categories1 =categories.objects.all()
    data = [{'categoriesName': category.categoriesName,'base_categories_name':category.base_categories.base_category_names,'is_active':category.is_active,'id': str(category.id)}
            for category in categories1]
    return JsonResponse(data, safe=False)


def base_category_list_view(request):
    return render(request, 'base_category_list.html')


def delete_category(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        base_category.objects.filter(id=category_id).delete()
        return JsonResponse({"message": "Category deleted successfully."})


def delete_subcategory(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        categories.objects.filter(id=category_id).delete()
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
    
def update_video_category(request):
    if request.method == "POST":
        video_id = request.POST.get("video_id")
        video_title = request.POST.get("videoName")
        video_link = request.POST.get("videoLink")
        base_categories_id = request.POST.get("base_categories_id")
        sub_categories_id = request.POST.get("sub_categories_id")
        print(video_id)

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

def get_data_changevideos(request):
    data = base_videos.objects.all()  
    data_list = [{'id':changevideos.id, 'title': changevideos.title,'link':changevideos.link,'base_categories_id':changevideos.base_categories.id,'base_categories_names':changevideos.base_categories.base_category_names,'is_active':changevideos.is_active,'categories_id':changevideos.categories.id,'categories_name':changevideos.categories.categoriesName}
                 for changevideos in data]
    return JsonResponse(data_list, safe=False)


def get_data_index_videos(request):   
    videos = base_videos.objects.all().order_by('-date_upload')[:10]
    video_data = []
    for video in videos:
        video_data.append({
            'link': video.link
        })
    return JsonResponse(video_data, safe=False)


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
    data = base_videos.objects.order_by('?')[:20]
    data_list = []
    for item in data:
        data_list.append({
            'title': item.title,
            'link': item.link,
        })
    return JsonResponse(data_list, safe=False)


def update_videos_activity(request):
    if request.method == "POST":
        video_id = request.POST.get("id")
        is_active = request.POST.get("active")
        try:
            category =  base_videos.objects.get(id=video_id)
            category.is_active = is_active
            category.date_update = timezone.now()
            category.save()
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

# altkategori düzenlemedeki base category
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

def videoUpdateGet(request):
    videoId = request.GET.get('videoId')
    print("----------"+videoId)
    videos = base_videos.objects.filter(id=videoId).values('title', 'link', 'categories','base_categories').first() 
    # videos = base_videos.objects.get(id=videoId)
    print("+++++++++"+videos['title'])
    data = []
    data.append({
        'title': videos['title'],
        'link': videos['link'],
        'categories': videos['categories'],
        'base_categories': videos['base_categories']
    })

    return JsonResponse(data, safe=False)