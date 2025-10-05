from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/list/',views.BlogListView.as_view(),name='blog_list'),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog_delete"),
]