from django.urls import path
from .views import index

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", index , name="index" ),
    path("principal/", views.principal , name='principal'),
    path('all_data/', views.view_all_data, name='view_all_data'),
    path('ofv/', views.clienteFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_nit>', views.updateView, name= 'update_url'),
    path('del/<int:f_nit>', views.deleteView, name= 'delete_url'),
    path("joins/", views.join_example, name='joins'),
]
