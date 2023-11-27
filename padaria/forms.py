from django import forms

from padaria.models import Cliente, Produto, Venda


# class ClienteForm(forms.Form):
#     nome = forms.CharField(max_length=30, required=True)
#     sobrenome = forms.CharField(max_length=50, required=True)
#     cpf = forms.CharField(max_length=14, required=True)
#     email = forms.EmailField(max_length=50, required=True)
#     pass

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email'
        ]
    pass


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome_produto',
            'descricao',
            'preco'
        ]
        labels = {
            'nome_produto': 'Produto',
            'descricao': 'Descrição',
            'preco': 'Preço'
        }

    pass

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = [
            'cliente',
            'produto'
        ]
        labels = {
            'cliente': 'Cliente',
            'produto': 'Produto'
        }



