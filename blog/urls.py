from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('categories/<slug>/', views.CategoryView.as_view(), name='blog-categories'),
    path('contributors/<int:user_id>/', views.Contributor.as_view(), name='blog-contributors'),
    path('posts/', views.PostList.as_view(), name='blog-post-list'),
    path('episodes/', views.EpisodeList.as_view(), name='blog-episode-list'),
    path('episodes/<slug>/', views.UniqueEpisode.as_view(), name='blog-episode'),
    path('posts/<slug>/', views.UniquePost.as_view(), name='blog-detail'),
    path('year/<int:year>/', views.year, name='blog-year'),
    path('year/<int:year>/month/<int:month>/', views.month, name='blog-month'),
]
