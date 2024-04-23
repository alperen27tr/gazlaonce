from django.urls import path
from . import base_category_views, views,base_videos_views,sub_category_views


urlpatterns= [
    #views
    path('get_data_subcategories', views.get_data_subcategories, name='get_data_subcategories'),
    path('get-data', views.get_data, name='get_data'),
    path('get-data_videos', views.get_data_videos, name='get_data_videos'),
    path('get_data_index_videos/', views.get_data_index_videos, name='get_data_index_videos'),
    path("",views.index,name="home"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("index",views.index),
    path("videos",views.videos,name="videos"),
    path("video_change",base_videos_views.video_change,name="video_change"),
    path('create-post/', views.create_post, name='create_post'),
    path('update_video_category', views.update_video_category, name='update_video_category'),
    path('get_data_base_category', views.get_data_base_category, name='get_data_base_category'),

    #base_category views
    path('get_data_header', base_category_views.get_data_header, name='get_data_header'),
    path("get_data_base_category1",base_category_views.get_data_base_category1,name="get_data_base_category1"),
    path('base_categories/', base_category_views.base_category_list_view, name='base_categories'),
    path("base_category_change",base_category_views.base_category_change,name="base_category_change"),
    path('get_categories/', base_category_views.get_categories, name='get_categories'),
    path('delete_category/', base_category_views.delete_category, name='delete_category'),
    path('update_category/', base_category_views.update_category, name='update_category'),
    path('update_base_category_activity/', base_category_views.update_base_category_activity, name='update_base_category_activity'),

    #base_videos views
    path("videoUpdateGet",base_videos_views.videoUpdateGet,name="videoUpdateGet"),
    path('create_post_video/', base_videos_views.create_post_video, name='create_post_video'),
    path('get_data_changevideos/', base_videos_views.get_data_changevideos, name='get_data_changevideos'),
    path('delete_base_videos_admin/', base_videos_views.delete_base_videos_admin, name='delete_base_videos_admin'),
    path('update_video_admin/', base_videos_views.update_video_admin, name='update_video_admin'),
    path('video_gallery_index/', base_videos_views.video_gallery_index, name='video_gallery_index'),
    path('update_videos_activity/', base_videos_views.update_videos_activity, name='update_videos_activity'),
    path('get_motocycle_videos/', base_videos_views.get_motocycle_videos, name='get_motocycle_videos'),
    path('get_data_opened_video_page_videos', base_videos_views.get_data_opened_video_page_videos, name='get_data_opened_video_page_videos'),  
    
    #sub_category views
    path("subcategory_change",sub_category_views.subcategory_change,name="subcategory_change"),
    path("get_subcategories/",sub_category_views.get_subcategories,name="get_subcategories"),
    path("create_post_subcategory/",sub_category_views.create_post_subcategory,name="create_post_subcategory"),
    path("delete_subcategory/",sub_category_views.delete_subcategory,name="delete_subcategory"),
    path('update_sub_category_activity/', sub_category_views.update_sub_category_activity, name='update_sub_category_activity'),
    path('get_data_subcategories_list', sub_category_views.get_data_subcategories_list, name='get_data_subcategories_list'),
    path('is_superuser/', sub_category_views.is_superuser, name='is_superuser'),

    #login page views
    path('login_page', views.login_page, name='login_page'),
    path('new_user_record', views.new_user_record, name='new_user_record'),
    path('login_view', views.login_view, name='login_view'),
    path('get_user_username_in_navbar', views.get_user_username_in_navbar, name='get_user_username_in_navbar'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    #signup page views
    path('signup_page', views.signup_page, name='signup_page'),
    
    
]

