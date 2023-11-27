from django.contrib.messages import success
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView

from padaria.forms import ClienteForm, ProdutoForm
from padaria.models import Cliente, Produto, Venda, Fila


# Create your views here.
def home(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        return render(requisicao, template_name='padaria/base.html')


def cria_cliente(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        form = ClienteForm()
        return render(requisicao, template_name='padaria/clientes/novo.html', context={'form': form})
    elif requisicao.method == 'POST':
        form = ClienteForm(requisicao.POST)
        if form.is_valid():
            cliente = Cliente(**form.cleaned_data)
            cliente.save()
            return HttpResponseRedirect(redirect_to='/')
        pass


def cria_produto(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        form = ProdutoForm()
        return render(requisicao, template_name='padaria/produtos/novoProduto.html', context={'form': form})
    elif requisicao.method == 'POST':
        form = ProdutoForm(requisicao.POST)
        if form.is_valid():
            produto = Produto(**form.cleaned_data)
            produto.save()
            return HttpResponseRedirect(redirect_to='/')
        else:
            return render(requisicao, template_name='padaria/produtos/parametro_invalido.html', context={'form': form})
        pass


def lista_clientes(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        clientes = Cliente.objetos.all()
        return render(requisicao, template_name='padaria/clientes/lista.html', context={'clientes': clientes})
    pass


def lista_produtos(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        produtos = Produto.objetos.all()
        return render(requisicao, template_name='padaria/produtos/lista.html', context={'produtos': produtos})
    pass


def detalhe_produto(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            produto = Produto.objetos.get(pk=pk)
        except Produto.DoesNotExist:
            produto = None

        return render(requisicao,template_name='padaria/produtos/detalhe.html', context={'produto': produto})


def atualiza_produto(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        produto = Produto.objetos.get(pk=pk)
        form = ProdutoForm(instance=produto)
        return render(requisicao, template_name='padaria/produtos/atualiza.html', context={'form': form})
    elif requisicao.method == 'POST':
        produto = Produto.objetos.get(pk=pk)
        form = ProdutoForm(requisicao.POST, instance=produto)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(redirect_to=f'/produtos/detalhe/{pk}')

class RemoveProdutoView(DeleteView):
    model = Produto
    template_name = 'padaria/produtos/remove.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('padaria:lista_produtos')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

class VendaListView(ListView):
    model = Venda
    template_name = 'padaria/vendas/lista.html'
    context_object_name = 'vendas'
    success_url = reverse_lazy('padaria:lista_vendas')

class VendaCreateView(CreateView):
    model = Venda
    template_name = 'padaria/vendas/novo.html'
    fields = ['cliente', 'produto']
    success_url = reverse_lazy('padaria:lista_vendas')


class AtualizaCreateView(UpdateView):
    model = Venda
    template_name = 'padaria/vendas/atualiza.html'
    fields = '__all__'
    context_object_name = 'venda'
    success_url = reverse_lazy('padaria:lista_vendas')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class RemoveVendaView(DeleteView):
    model = Venda
    template_name = 'padaria/vendas/remove.html'
    fields = '__all__'
    context_object_name = 'venda'
    success_url = reverse_lazy('padaria:lista_vendas')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


