from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import categories,base_videos,base_category
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "gazlaonce_p/index.html")

def videos(request):
    return render(request,"gazlaonce_p/videos.html")

def login_page(request):
    return render(request, "gazlaonce_p/login_page.html")

def signup_page(request):
    return render(request, "gazlaonce_p/signup_page.html")

def dashboard(request):
    return render(request, "gazlaonce_p/dashboard.html")

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
    videos = base_videos.objects.all().order_by('-date_upload')[:5]
    video_data = []
    for video in videos:
        video_data.append({
            'link': video.link
        })
    return JsonResponse(video_data, safe=False)

def get_data_base_category(request):
    videos_data = base_category.objects.filter(is_active="True").values('base_category_names','id') 
    data = []
    for video in videos_data:
        data.append({
            'base_category_names': str(video['base_category_names']),
            'id': str(video['id']),
        })
    return JsonResponse(data, safe=False)


def new_user_record(request):
    print("efsfds")
    if request.method == 'POST':
        NewUserName = request.POST.get('username')
        NewPassword = request.POST.get('password')
        NewMail=request.POST.get('email')
        NewName=request.POST.get('first_name')
        NewSurname=request.POST.get('last_name')

       

        user = User.objects.create(username=NewUserName, email=NewMail,first_name=NewName,last_name=NewSurname)

        user.set_password(NewPassword)
        user.save()
        return JsonResponse({'message': 'Kullanıcı başarıyla kaydedildi.'})
    else:
        return JsonResponse({'message': 'Sadece POST istekleri kabul edilir.'})

def login_view(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
        #  firstname=request.POST['first_name']
         print(username,password)
         user = authenticate(request, username=username, password=password)
         print(user)
         if user is not None:
             login(request, user)
             return JsonResponse({'message': 'Giriş Başarılı...', 'status': '0'})
         else:
             return JsonResponse({'message': 'Kullanıcı Adı Veya Şifre Yanlış', 'status': '1'})

@login_required
def get_user_username_in_navbar(request):
    user_name = request.user.username
    return JsonResponse({'username': user_name})

def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Çıkış yapıldı'})

def admin_dashboard(request):
    superusers = User.objects.filter(is_superuser=1)
    return render(request, 'admin_dashboard.html', {'superusers': superusers})

def for_play_bigVideo_get_database(request):
    videos = base_videos.objects.filter(link=VideoLink)
    return render(request, 'videos.html', {'videos': videos})

