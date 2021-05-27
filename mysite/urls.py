
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mysite.core import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('files/', views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('files/<int:pk>', views.start, name='start'),
    path('save/', views.save, name='save'),
    path('about/',views.about, name="about"),
    path('tutorial/',views.tutorial, name="tutorial"),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

