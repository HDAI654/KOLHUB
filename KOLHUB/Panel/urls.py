from django.urls import path, include
from .views import *

urlpatterns = [
    path('Panel', show_panel, name='show user panel'),
    path('html_file_to_page', upload_html_file, name='create page from html file'),
    path('code_to_page', upload_html_text, name='create page from code'),
    path('pages/xx/<str:user>/<int:page_id>', show_page, name='show page'),
    path('del_page/<str:user>/<int:page_id>', delete_page, name='delete page'),
    
    ]