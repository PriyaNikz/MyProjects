from . import views
from django.urls import path
app_name='moviesapp1'

urlpatterns = [
    path('', views.index,name="index"),
    path('movie/<int:movie_id>/',views.detail,name="detail"),
    path('add/',views.add_movies,name="add_movies"),
    path('update/<int:movie_id>/',views.update,name="update"),
    path('delete/<int:movie_id>/',views.delete,name="delete")
]