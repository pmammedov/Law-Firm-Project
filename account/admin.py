from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name', 'last_name','country',)
    search_fields = ('first_name','email','last_name') 
 
    actions = ['verify','unverify','activate' ,'deactivate' ]
    
    def verify(self, queryset):
        queryset.update(is_verified=True)
        
    def unverify(self, queryset):
        queryset.update(is_verified=False)
        
    def activate(self, queryset):
        queryset.update(is_active=True)
        
    def deactivate(self, queryset):
        queryset.update(is_active=False)

@admin.register(LawyerType)
class LawyerTypeAdmin(admin.ModelAdmin):
    list_display = ('name','updated',  )
    search_fields = ('name',) 
 
@admin.register(Lawywer)
class LawywerAdmin(admin.ModelAdmin):
    list_display = ('user','fee','experience', 'organisation', )
    search_fields = ('user.email','fee','organisation',) 

@admin.register(Apointment)
class ApointmentAdmin(admin.ModelAdmin):
    list_display = ('subject','lawyer','client','startTime', 'endtTime', )
    search_fields = ('startTime','endtTime','subject') 

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ( 'lwyr','usr','rate', 'updated', )
    search_fields = ('rate','updated', ) 

