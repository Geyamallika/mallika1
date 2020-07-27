from django.urls import path
from Myapp import views
app_name="Myapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
]
