from django.contrib import admin
from . models import Blogpost
# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','is_completed')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Blogpost,BlogpostAdmin)