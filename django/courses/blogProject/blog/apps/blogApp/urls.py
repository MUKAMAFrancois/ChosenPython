from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('blog/<int:blog_id>/', views.detailed_page, name='detailed_page'),
    path('create_blog/', views.create_blog_post, name='create_blog')
    

]