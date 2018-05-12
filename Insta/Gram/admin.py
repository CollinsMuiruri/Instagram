from django.contrib import admin
from .models import Image,tag

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag')
# Register your models here.
admin.site.register(Image)
admin.site.register(tag)
