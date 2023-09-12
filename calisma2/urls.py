
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name="indexPage"),
    path('detail/<idcard>', views.detailPage, name="detailPage"),
    path('category', views.categoryPage, name="categoryPage"),
    path('category/<categorytitle>', views.categoryPage, name="categoryPage"),
    path('form', views.formPage, name="formPage"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)