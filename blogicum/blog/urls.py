from blog import views
from django.urls import path


app_name = 'blog'

urlpatterns = [
    path('', views.index, {'flag': False}, name='index'),
    path('posts/<int:post_id>/', views.post_detail,
         {'flag': True}, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
]
