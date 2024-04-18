from django.urls import path
from . import views
import uuid

urlpatterns = [

    path('home',views.homepage,name='homepage'),
    path('all',views.list_posts,name='listofposts'),

    path('post/<int:post_id>',views.single_post,name='singlepost'),

    # serializers

    path('',views.Post_ListCreate.as_view(),name='post_list'),

    path('<uuid:pk>',views.Post_RetrieveUpdateDestroy.as_view(),name='post_detail'),
    
]
