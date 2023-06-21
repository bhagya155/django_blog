from django.urls import path 
from . import views


urlpatterns = [
    path('write_blog', views.write_blog,name='write_blog'),
    path('view_blog', views.view_blog,name='view_blog'),
    path('read_blog/<int:id>', views.read_blog,name='read_blog'),
    path('add_blog', views.add_blog,name='add_blog'),
    path('edit_blog\<int:id>', views.edit_blog,name='edit_blog'),

]