from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ContactData)

class Contact_DataModelAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'name',
        'email',
        'contact'
    ]
    list_display = ['id','name', 'email','contact','message']

@admin.register(project_cms)

class Project_CMS_Admin(admin.ModelAdmin):
    search_fields = [
        'title',
        'pdate',
     ]
    list_display = ['title','image','pdate']

@admin.register(blog_cms)

class Blog_Cms_Admin(admin.ModelAdmin):
    search_fields = [
        'blog_date',
        'bloger_name',
        'blog_discription',
        'blog_title'
    ]
    list_display = ['blog_title', 'blog_discription',  'blog_image','blog_date', 'bloger_name']