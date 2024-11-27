from django.contrib import admin
from .models import UsersModel,TaskModel
# Register your models here.
@admin.register(UsersModel)
class UsersAdmin(admin.ModelAdmin):
    list_display=['name','age','email','phone','created_at']
    search_fields=['name','age','email','phone','created_at']
@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display=['user','title','created_at','description','status','image']
    search_fields=['user','title','created_at','description','status','image']
    list_editable=['status']