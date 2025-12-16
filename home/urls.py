from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('produto/<slug:produto_slug>/', views.detalhe_produto , name='detalhe_produto'),
    path('categoria/<slug:slug_categoria>/', views.filtro ,name='filtro'),
    path('carrinho/', views.carrinho , name='carrinho'),
    path('add-carrinho/', views.add_carrinho, name='add-carrinho' ),
    path('excluir/<int:item>/', views.excluir_item , name='excluir_item')
]