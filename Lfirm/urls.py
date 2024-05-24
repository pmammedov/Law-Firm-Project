from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path,include
from blog.views import *

urlpatterns = [
    path("",HomeScreen.as_view( template_name='blog/home.html' ) ,name='home'),
    path("blog/",include('blog.urls')),
    path("admin/", admin.site.urls),
    path("contact/",ContactFunc,name = 'contact'),
    path("account/",include('account.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
