from django.contrib import admin

from .models import  *

 
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','updated')
    search_fields = ('title', 'body') 
  
    actions = ['activate' ,'deactivate' ]
       
    def activate(self, request, queryset):
        queryset.update(active=True)
        
    def deactivate(self, request, queryset):
        queryset.update(active=False)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name', 'email','body')
    search_fields = ('name', 'email','body') 
  
    actions = ['activate' ,'deactivate' ]
       
    def activate(self, request, queryset):
        queryset.update(active=True)
        
    def deactivate(self, request, queryset):
        queryset.update(active=False)
