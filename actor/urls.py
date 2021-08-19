from django.urls import path
from actor import views

app_name = 'actor'
urlpatterns = [
    # Example: /actor/
    path('', views.ActorLV.as_view(), name='index'),

    # Example: /actor/
    path('actor', views.ActorLV.as_view(), name='actor_list'),

    # Example: /actor/99
    path('<int:pk>/', views.ActorDV.as_view(), name='actor_detail'),

    # Example: /actor/add/
    path('add/', views.ActorCV.as_view(), name='actor_add'),

    # Example: /actor/change/
    path('change/', views.ActorChangeLV.as_view(), name='actor_change'),

    # Example: /actor/99/update/
    path('<int:pk>/update/', views.ActorUV.as_view(), name='actor_update'),

    # Example: /actor/99/delete/
    path('<int:pk>/delete/', views.ActorDelV.as_view(), name='actor_delete'),

]