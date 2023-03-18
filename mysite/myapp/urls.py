from django.urls import path

from . import views


app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    
    path('my_chat_bot/', views.My_chat_botView.as_view(), name="my_chat_bot"),
    
    path('myapp-list/', views.MyappListView.as_view(), name="myapp_list"),
    path('myapp-detail/<int:pk>/', views.MyappDetailView.as_view(), name="myapp_detail"),
    path('myapp-create/', views.MyappCreateView.as_view(), name="myapp_create"),
    path('myapp-update/<int:pk>/', views.MyappUpdateView.as_view(), name="myapp_update"),
    path('myapp-delete/<int:pk>/', views.MyappDeleteView.as_view(), name="myapp_delete"),
]
