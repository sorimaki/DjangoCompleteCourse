from django.contrib import admin
from django.urls import path, include
from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('<int:id>/', views.google),
    path('global/', views.global1)
] 

admin.site.site_header = 'Django Blog course'
admin.site.index_title = 'Blog Course: Administration pannel'