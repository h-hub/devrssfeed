from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('bookmark', views.bookmarks, name='bookmarks'),
    path('ajax/bookmark', views.add_bookmark, name='bookmark'),
    path('ajax/is_bookmark', views.is_bookmark, name='bookmark'),
    # path('$/', views.authors, name='authors'),
    # path('$/', views.links, name='links'),
]