from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.AllView.as_view()),
    path('post/create', views.PostCreate.as_view()),
    path('post/get_top', views.GetTopPosts.as_view()),
    path('rating/set', views.RatingSet.as_view()),
]