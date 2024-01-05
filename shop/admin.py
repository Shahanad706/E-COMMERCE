from django.contrib import admin
from shop.models import *
# Register your models here.

class categAdmin(admin.ModelAdmin):
    list_display =['name','slug']

    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,categAdmin)

class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','img']

    list_editable = ['price','stock','available','img']

    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodAdmin)