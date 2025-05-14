from django.urls import path

from menu import views

app_name = 'category'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:parent_slug>/', views.categories, name='parent'),
    path('category/<slug:parent_slug>/<slug:child_slug>/', views.categories, name='child'),
]
