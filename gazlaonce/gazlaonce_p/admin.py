from django.contrib import admin
from .models import categories,base_videos,base_category

class gazlaonceAdmin(admin.ModelAdmin):
    #list_display=("title","is_active","is_home",)
    #list_editable=("is_active","is_home",)
    #search_fields=("title","description",)
    pass

admin.site.register(categories,gazlaonceAdmin)
admin.site.register(base_category)
admin.site.register(base_videos)