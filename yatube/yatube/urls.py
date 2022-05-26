from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from posts import views

urlpatterns = [
    # импорт правил из приложения posts
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
