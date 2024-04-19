from django.urls import path
from . import views
import uuid

urlpatterns = [

    # path('home',views.homepage,name='homepage'),
    path('all',views.list_posts,name='listofposts'),
    path('create',views.create_a_post,name='createpost'),
    path('post/<uuid:post_id>',views.single_post,name='singlepost'),
    path('post/<uuid:post_id>/update',views.update_post,name='updatepost'),
    path('post/<uuid:post_id>/delete',views.delete_post,name='deletepost'),


    # serializers
    # path('',views.Post_ListCreate.as_view(),name='post_list'),

    # path('<uuid:pk>',views.Post_RetrieveUpdateDestroy.as_view(),name='post_detail'),
    
]
