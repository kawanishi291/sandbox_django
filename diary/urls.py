from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary_list/', views.DiaryList.as_view(), name="diary_list"),
    path('diary_create/', views.DiaryCreate.as_view(), name="diary_create"),
    path('diary_detail/<int:pk>/', views.DiaryDetail.as_view(), name="diary_detail"),
    path('diary_update/<int:pk>/', views.DiaryUpdate.as_view(), name="diary_update"),
    path('diary_delete/<int:pk>/', views.DiaryDelete.as_view(), name="diary_delete"),
]