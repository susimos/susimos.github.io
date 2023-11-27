from django.conf.urls.static import static
from django.urls import path
from django.views.generic import ListView

from core import settings
from padaria.views import home, cria_cliente, cria_produto, lista_clientes, lista_produtos, detalhe_produto, \
    atualiza_produto, RemoveProdutoView, VendaListView, VendaCreateView, AtualizaCreateView, RemoveVendaView

app_name = 'padaria'

urlpatterns = [
    path('', home),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('produtos/parametro_invalido', cria_produto),
    path('produtos/detalhe/<pk>', detalhe_produto),
    path('produtos/atualiza/<pk>', atualiza_produto, name='produtos_atualiza'),
    path('clientes/', lista_clientes),
    path('clientes/novo', cria_cliente),
    path('produtos/novoProduto', cria_produto),
    path('produtos/remove/<pk>', RemoveProdutoView.as_view(), name='remove_produto'),

    #Vendas
    path('vendas/', VendaListView.as_view(), name='lista_vendas'),
    path('vendas/novo', VendaCreateView.as_view(), name='nova_venda'),
    path('vendas/atualiza/<pk>', AtualizaCreateView.as_view(), name='atualiza_venda'),
    path('vendas/remove/<pk>', RemoveVendaView.as_view(), name='remove_venda'),

    # #Fila
    # path('fila/', FilaListView.as_view(), name='lista_fila'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
