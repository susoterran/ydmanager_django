from django.urls import path
from label import views

app_name = 'label'
urlpatterns = [
    # Example: /label/
    path('', views.LabelLV.as_view(), name='index'),

    # Example: /label/
    path('label', views.LabelLV.as_view(), name='label_list'),

    # Example: /label/99
    path('<int:pk>/', views.LabelDV.as_view(), name='label_detail'),

    # Example: /label/add/
    path('add/', views.LabelCV.as_view(), name='label_add'),

    # Example: /label/change/
    path('change/', views.LabelChangeLV.as_view(), name='label_change'),

    # Example: /label/99/update/
    path('<int:pk>/update/', views.LabelUV.as_view(), name='label_update'),

    # Example: /label/99/delete/
    path('<int:pk>/delete/', views.LabelDelV.as_view(), name='label_delete'),

]