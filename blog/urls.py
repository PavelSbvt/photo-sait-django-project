from django.urls import path, include  # добавьте include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('base/', views.post_list, name='base'),  # Главная страница
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),

    # Добавьте эту строку для аутентификации:
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/<int:pk>/like/', views.like_post, name='like_post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)