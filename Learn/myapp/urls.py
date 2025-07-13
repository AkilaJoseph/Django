from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # # path('news_detail/', views.news_detail, name='news_detail'),
    # path('blog/', views.blog, name="blog"),
    # path('cart/', views.cart, name="cart"),
    
]