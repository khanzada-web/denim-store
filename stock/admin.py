from django.contrib import admin
from stock.models import item


class registry(admin.ModelAdmin):
     list_display=('icon_Image','catagory','Name','price')

admin.site.register(item,registry)

